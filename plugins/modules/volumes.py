#!/usr/bin/python3
# Copyright ©️ 2022 Dell Inc. or its subsidiaries.
from __future__ import (absolute_import, division, print_function)
import urllib3
urllib3.disable_warnings()
import json
import sys

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.volumes_api import VolumeApi
__metaclass__ = type


DOCUMENTATION = r'''
module: volumes
short_description: 'This module allows to work with NetWorker Volumes'
description: 'This module allows to work with NetWorker Volumes'
version_added: '2.0.0'
options:
  state:
    type: str
    choices:
    - removeFileIndex, delete, changeLocation, get, recycle, markScanRequired, changeMode
    required: true
    description: 'Choose one of the state from above choices.'
  location:
    type: str
    description: 'Use this option when you want to change the location of volume'
  name:
    type: str
    description: 'Name of the volume'
  mode:
    type: str
    choices:
    - ReadOnly, Appendable, Recyclable
    description: 'Use this option when you want to change the mode'
  query_params:
    type: dict
    description: 'Use this attribute if you want to filter the resources as per parameter values.'
  field_params:
    type: list
    description: 'Use this attribute if you want to list only perticular fields'  

'''

EXAMPLES = r'''
    - name: Get all Volume information
      dellemc.networker.volumes:
        state: get
      register: volumes
    - name: Get volume information by volume name
      dellemc.networker.volumes:
        state: get
        query_params:
          name: VOLNAME.001
'''


def remove_none(obj):
  if isinstance(obj, (list, tuple, set)):
    return type(obj)(remove_none(x) for x in obj if x is not None)
  elif isinstance(obj, dict):
    return type(obj)((remove_none(k), remove_none(v))
      for k, v in obj.items() if k is not None and v is not None)
  else:
    return obj


def main():
    fields = {
        'state': {'type': 'str', 'choices': ['removeFileIndex', 'delete', 'changeLocation', 'get', 'recycle', 'markScanRequired', 'changeMode'], 'required': True},
        'location': {'type': 'str'},
        'volumeId': {'type': 'str'},
        'mode': {'type': 'str', 'choices': ['ReadOnly', 'Appendable', 'Recyclable']},
        'field_params': {'type': 'list'},
        'query_params': {'type': 'dict'},
        'host': {'type': 'str', 'required': False},
        'port': {'type': 'int', 'default': 9090},
        'username': {'type': 'str', 'required': False},
        'password': {'type': 'str', 'no_log': False}
    }
    module = AnsibleModule(argument_spec=fields, required_if=[('state', 'changeMode', 'mode', False),
                                                              ('state', 'changeLocation', 'location', False)])
    server = module.params['host']
    user = module.params['username']
    port = module.params['port']
    password = module.params['password']
    state = module.params['state']
    auth = (user, password)
    keys_to_delete = ['host', 'username', 'port', 'password']
    for key in keys_to_delete:
        if key in module.params:
            del module.params[key]
    params = remove_none(module.params)
    url = url = f'https://{server}:{port}/nwrestapi/v3/global'
    failed, changed, msg, resp_msg = False, False, "", dict()
    resp_msg['responses'] = []
    resp_msg['msg'] = []
    api_initialize = VolumeApi(auth=auth, url=url)
    try:
        module.params['password'] = module.params.pop('remoteUserPassword')
    except Exception as e:
        pass
    if state == 'get':
        if module.params['volumeId'] is not None:
            if len(module.params['volumeId']) > 0:
                volume_name = module.params['volumeId']
                response = api_initialize.get_volume(volume_id=volume_name, field_params=module.params['field_params'])
                resp_msg['responses'].append(response)
        else:
            response = api_initialize.get_volumes(field_params=module.params['field_params'], query_params=module.params['query_params'])
            resp_msg['responses'].append(response)
    elif state == 'removeFileIndex':
        volume_name = module.params['volumeId']
        body = params
        del body['state']
        body['operationValue'] = None
        response = api_initialize.post_remove_volume_from_file_index(volume_id=volume_name, body=body)
        resp_msg['responses'].append(response)
        msg = 'Storage Node %s Created Successfully' % volume_name
        resp_msg['msg'].append(msg)

    elif state == 'changeLocation':
        volume_name = module.params['volumeId']
        body = params
        del body['state']
        body['operationValue'] = None
        response = api_initialize.post_remove_volume_from_file_index(volume_id=volume_name, body=body)
        resp_msg['responses'].append(response)
        msg = 'Storage Node %s Created Successfully' % volume_name
        resp_msg['msg'].append(msg)
    elif state == 'recycle':
        volume_name = module.params['volumeId']
        body = params
        del body['state']
        body['operationValue'] = "AutoRecycle"
        response = api_initialize.post_remove_volume_from_file_index(volume_id=volume_name, body=body)
        resp_msg['responses'].append(response)
        msg = 'Storage Node %s Created Successfully' % volume_name
        resp_msg['msg'].append(msg)
    elif state == 'markScanRequired':
        volume_name = module.params['volumeId']
        body = params
        del body['state']
        body['operationValue'] = "ScanNeeded"
        response = api_initialize.post_remove_volume_from_file_index(volume_id=volume_name, body=body)
        resp_msg['responses'].append(response)
        msg = 'Storage Node %s Created Successfully' % volume_name
        resp_msg['msg'].append(msg)
    elif state == 'changeMode':
        volume_name = module.params['volumeId']
        body = params
        del body['state']
        if module.params['mode'] is not None:
            body['operationValue'] = module.params['mode']
            response = api_initialize.post_remove_volume_from_file_index(volume_id=volume_name, body=body)
            resp_msg['responses'].append(response)
            msg = 'Storage Node %s Created Successfully' % volume_name
            resp_msg['msg'].append(msg)

    elif state == 'delete':
        volume_name = module.params['volumeId']
        response = api_initialize.delete_volume(volume_id=volume_name)
        resp_msg['responses'].append(response)
        msg = 'Storage Node %s deleted Successfully' % volume_name
        resp_msg['msg'].append(msg)

    api_responses = []
    success_codes = [200, 201, 202, 204]
    i = 0
    for response in resp_msg['responses']:
        status_code = response.status_code
        if status_code in success_codes:
            api_response = response.text
            if len(api_response) == 0:
                api_response = resp_msg['msg'][i]
                changed = True
            else:
                api_response = json.loads(api_response)
                changed = False
            failed = False
        elif "There is already a" in response.text:
            changed = False
            failed = False
            api_response = eval(response.text)['message'] + '. Skipping addition..'
        else:
            failed = True
            changed = False
            api_response = json.loads(response.text)
        i += 1
        api_responses.append(api_response)
    module.exit_json(failed=failed, msg=api_responses, changed=changed)


if __name__ == '__main__':
    main()



#!/usr/bin/python3
# Copyright ©️ 2022 Dell Inc. or its subsidiaries.
from __future__ import (absolute_import, division, print_function)
import urllib3
urllib3.disable_warnings()
import json
import sys
from ansible.module_utils.basic import AnsibleModule
sys.path.insert(0, '/opt/collections/dellemc/networker/')
from plugins.module_utils.nasdevices_api import nasDevicesApi
__metaclass__ = type


DOCUMENTATION = r'''
module: lockboxes
short_description: 'This module allows you to work with networker nasdevices'
description: 'Use this module to create, delete, modify nasdevices on networker server'
version_added: '2.0.0'
options:
  state:
    type: str
    choices:
    - create, delete, modify, get
    required: true
    description: 'Specify the action you want to take. e.g for creating nasdevice template, use create'
  name: 
    type: str
    description: 'Name of the NAS Device'
  comment:
    type: str
    description: 'Any user defined description of this NAS device'
  nasDeviceManagementName:
    type: str
    description: 'The management name of the NAS device.'
  nasManagementPassword:
    type: str
    description: 'his password is used to perform management actions on a NAS device. If a password is given, then the "NAS management user" attribute must also be defined.'
  nasManagementUser:
    type: str
    description: 'The user as which to run remote management commands on this NAS device.'
  query_params:
    type: dict
    description: 'Use this attribute if you want to filter the resources as per parameter values.'
  field_params:
    type: list
    description: 'Use this attribute if you want to list only perticular fields'  
auther: 
    Sudarshan Kshirsagar (@kshirs1)
'''

EXAMPLES = r'''
- name: Get all nasdevices
  dellemc.networker.nasdevices:
    state: get
    
- name: Get Nasdevice based on query.
  dellemc.networker.nasdevices:
    state: get
    query_params:
      "nasDeviceManagementName": "nadevice.com"

- name: Create nasdevice
  dellemc.networker.nasdevices:
    state: create
    name: nasdevice.com
    nasDeviceManagementName: nasmgmtuser
    nasManagementPassword: password01
    nasManagementUser: nasuser
    
- name: modify nasdevice
  dellemc.networker.nasdevices:
    state: modify
    name: nasdevice.com
    nasDeviceManagementName: nasmgmtuser
    nasManagementPassword: password01
    
- name: delete nasdevice
  dellemc.networker.nasdevices:
    state: delete
    name: nasdevice.com
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
        'state': {'type': 'str', 'choices': ['create', 'delete', 'modify', 'get'], 'required': True},
        'comment': {'type': 'str'},
        'name': {'type': 'str'},
        'nasDeviceManagementName': {'type': 'str'},
        'nasManagementPassword': {'type': 'str', 'no_log': False},
        'nasManagementUser': {'type': 'str'},
        'query_params': {'type': 'dict'},
        'field_params': {'type': 'list'},
        'host': {'type': 'str', 'required': False},
        'port': {'type': 'int', 'default': 9090},
        'username': {'type': 'str', 'required': False},
        'password': {'type': 'str', 'no_log': False}
    }
    module = AnsibleModule(argument_spec=fields)
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
    url = f'https://{server}:{port}/nwrestapi/v3/global'
    failed, changed, msg, resp_msg = False, False, "", dict()
    resp_msg['responses'] = []
    resp_msg['msg'] = []
    api_initialize = nasDevicesApi(auth=auth, url=url)

    if state == 'get':
        if module.params['name'] is not None:
            if len(module.params['name']) > 0:
                nasdevice_name = module.params['name']
                response = api_initialize.get_nasdevice(nasdevice_id=nasdevice_name)
                resp_msg['responses'].append(response)
        else:
            response = api_initialize.get_nasdevices(query_params=module.params['query_params'], field_params=module.params['field_params'])
            resp_msg['responses'].append(response)
    elif state == 'create':
        nasdevice_name = module.params['name']
        body = params
        del body['state']
        response = api_initialize.post_nasdevice(body=body)
        resp_msg['responses'].append(response)
        msg = 'nasdevice %s Created Successfully' % nasdevice_name
        resp_msg['msg'].append(msg)
    elif state == 'modify':
        nasdevice_name = module.params['name']
        body = params
        del body['state']
        response = api_initialize.put_nasdevice(body=body, nasdevice_id=nasdevice_name)
        resp_msg['responses'].append(response)
        msg = 'nasdevice %s modified Successfully' % nasdevice_name
        resp_msg['msg'].append(msg)
    elif state == 'delete':
        nasdevice_name = module.params['name']
        response = api_initialize.delete_nasdevice(nasdevice_id=nasdevice_name)
        resp_msg['responses'].append(response)
        msg = 'nasdevice %s deleted Successfully' % nasdevice_name
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
            api_response = eval(response.text)['message']
        else:
            failed = True
            changed = False
            api_response = json.loads(response.text)
        i += 1
        api_responses.append(api_response)
    module.exit_json(failed=failed, msg=api_responses, changed=changed)


if __name__ == '__main__':
    main()



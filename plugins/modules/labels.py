#!/usr/bin/python3
# Copyright ©️ 2022 Dell Inc. or its subsidiaries.
from __future__ import (absolute_import, division, print_function)
import urllib3
urllib3.disable_warnings()
import json
import sys

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.labels_api import LabelsApi
__metaclass__ = type


DOCUMENTATION = r'''
module: labels
short_description: 'This module allows you to work with networker Label templates'
description: 'Use this module to create, delete, modify label template or get the information about it'
version_added: '2.0.0'
options:
  state:
    type: str
    choices:
    - create, delete, modify, get
    required: true
    description: 'Specify the action you want to take. e.g for creating label template, use create'
  comment:
    type: str
    description: 'Any user defined description of this label or other explanatory remarks'
  name:
    type: str
    description: 'Name of the label template'
  fields:
    type: list
    description: "List of label components. Each component must be either a `list of strings', a `numeric range', a `lower-case range', or an `upper-case range'. See the NetWorker Administrator's Guide for more details"
  next:
    type: str
    description: 'The next label that this template will generate. After it is used, a new label will be generated and stored here. By default, the first value in each of the constituent fields is used to create the first name.'
  separator:
    type: str
    description: ' The character to insert between label components'
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
- name: Creating Label Templates
  dellemc.networker.label:
    state: create
    name: A001S
    fields:
      - A001S
      - 00-99
    separator: .

- name: Deleting Label Template
  dellemc.networker.label:
    state: delete
    name: A001S
    
- name: Get information about Label Template
  dellemc.networker.label:
    state: get
    name: A001S
    
- name: Modify Field and/or separator Label Templates
  dellemc.networker.label:
    state: create
    name: A001S
    fields:
      - A001S
      - 000-999
    separator: -
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
        'fields': {'type': 'list'},
        'next': {'type': 'str'},
        'separator': {'type': 'str'},
        'field_params': {'type': 'list'},
        'query_params': {'type': 'dict'},
        'host': {'type': 'str', 'required': False},
        'port': {'type': 'int', 'default': 9090},
        'username': {'type': 'str', 'required': False},
        'password': {'type': 'str', 'no_log': False}
    }
    module = AnsibleModule(argument_spec=fields,
                           mutually_exclusive=('user-group', 'server-config', 'audit-log-config', 'server-stats'))
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
    api_initialize = LabelsApi(auth=auth, url=url)

    if state == 'get':
        if module.params['name'] is not None:
            if len(module.params['name']) > 0:
                label_name = module.params['name']
                response = api_initialize.get_label(label_id=label_name, field_params=module.params['field_params'])
                resp_msg['responses'].append(response)
        else:
            response = api_initialize.get_labels(field_params=module.params['field_params'], query_params=module.params['query_params'])
            resp_msg['responses'].append(response)
    elif state == 'create':
        label_name = module.params['name']
        body = params
        del body['state']
        response = api_initialize.post_label(body=body)
        resp_msg['responses'].append(response)
        msg = 'Protection Group %s Created Successfully' % label_name
        resp_msg['msg'].append(msg)
    elif state == 'modify':
        label_name = module.params['name']
        body = params
        del body['state']
        response = api_initialize.put_label(body=body, label_id=label_name)
        resp_msg['responses'].append(response)
        msg = 'Protection Group %s modified Successfully' % label_name
        resp_msg['msg'].append(msg)

    elif state == 'delete':
        label_name = module.params['name']
        response = api_initialize.delete_label(label_id=label_name)
        resp_msg['responses'].append(response)
        msg = 'Protection Group %s deleted Successfully' % label_name
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



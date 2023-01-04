#!/usr/bin/python3
# Copyright ©️ 2022 Dell Inc. or its subsidiaries.
from __future__ import (absolute_import, division, print_function)
import urllib3
urllib3.disable_warnings()
import json
import sys
from ansible.module_utils.basic import AnsibleModule
from ..module_utils.lockboxes_api import lockboxesApi
__metaclass__ = type


DOCUMENTATION = r'''
module: lockboxes
short_description: 'This module allows you to work with networker lockboxes'
description: 'Use this module to create, delete, modify lockboxes on networker server'
version_added: '2.0.0'
options:
  state:
    type: str
    choices:
    - create, delete, modify, get
    required: true
    description: 'Specify the action you want to take. e.g for creating lockbox, use create'
  name: 
    type: str
    description: 'A symbolic name that uniquely identifies this NSR lockbox. Cannot include any characters from the following list: "\?/*:><"|;" and cannot be neither "." nor ".."'
  client:
    type: str
    description: 'The name of the NSR client who owns this lockbox.'
  users:
    type: list
    description: ' List of users who can access the data in this lockbox. Uses userlist format, ie. user@host, or user=<user>,host=<host>'
  externalRoles:
    type: list
    description: 'List of externally authenticated users and roles allowed to access data in this lockbox, in the full DN format.'
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
- name: Get all lockboxes
  dellemc.networker.lockbox:
    state: get
    
- name: Get lockboxes for perticular client.
  dellemc.networker.lockbox:
    state: get
    query_params:
      "client": "clientName"

- name: Create Lockbox
  dellemc.networker.lockbox:
    state: create
    name: oracle19-02
    client: oracle19-02
    users:
      - "user=root,host=backupserver"
      - "user=administrator,host=backupserver""
    externalRoles:
      - cn=Administrators,cn=Groups,dc=backupserver,dc=dc01,dc=dc,dc=com

- name: modify lockbox
  dellemc.networker.lockbox:
    state: modify
    name: oracle19-02
    users:
      - "user=root,host=bacli[server"
      - "user=administrator,host=backupserver"
    externalRoles:
      -
- name: delete lockbox
  dellemc.networker.lockbox:
    state: delete
    name: oracle19-02
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
        'client': {'type': 'str'},
        'name': {'type': 'str'},
        'users': {'type': 'list'},
        'externalRoles': {'type': 'list'},
        'query_params': {'type': 'dict'},
        'field_params': {'type': 'list'},
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
    url = f'https://{server}:{port}/nwrestapi/v3/global'
    failed, changed, msg, resp_msg = False, False, "", dict()
    resp_msg['responses'] = []
    resp_msg['msg'] = []
    api_initialize = lockboxesApi(auth=auth, url=url)

    if state == 'get':
        if module.params['name'] is not None:
            if len(module.params['name']) > 0:
                lockbox_name = module.params['name']
                response = api_initialize.get_lockbox(lockbox_id=lockbox_name)
                resp_msg['responses'].append(response)
        else:
            response = api_initialize.get_lockboxes(query_params=module.params['query_params'], field_params=module.params['field_params'])
            resp_msg['responses'].append(response)
    elif state == 'create':
        lockbox_name = module.params['name']
        body = params
        del body['state']
        response = api_initialize.post_lockbox(body=body)
        resp_msg['responses'].append(response)
        msg = 'Lockbox %s Created Successfully' % lockbox_name
        resp_msg['msg'].append(msg)
    elif state == 'modify':
        lockbox_name = module.params['name']
        body = params
        del body['state']
        response = api_initialize.put_lockbox(body=body, lockbox_id=lockbox_name)
        resp_msg['responses'].append(response)
        msg = 'Lockbox %s modified Successfully' % lockbox_name
        resp_msg['msg'].append(msg)

    elif state == 'delete':
        lockbox_name = module.params['name']
        response = api_initialize.delete_lockbox(lockbox_id=lockbox_name)
        resp_msg['responses'].append(response)
        msg = 'Lockbox %s deleted Successfully' % lockbox_name
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



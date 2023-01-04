#!/usr/bin/python3
# Copyright ©️ 2022 Dell Inc. or its subsidiaries.
from __future__ import (absolute_import, division, print_function)
import urllib3
urllib3.disable_warnings()
import json
from ansible.module_utils.basic import AnsibleModule
from ..module_utils.directives_api import DirectivesApi

__metaclass__ = type

DOCUMENTATION = r'''
module: directives
short_description: 'This module allows to work with NetWorker directives'
description: 'This operation can be used to delete the specific directive.<br><br> Directives can be created to provide special instructions at the client level. A directive can be defined to skip certain directories or file types, to compress backup data, or to encrypt backup data.'
version_added: '2.0.0'
options:
  state:
    type: str
    choices:
    - create, delete, modify, get
    required: true
    description: 'Use this field to specify the action to take on media pool.'
  name:
    type: str
    description: 'The name of the directive must be unique on this server'
  comment:
    type: str
    description: 'Any user defined description of this directive or other explanatory remarks.'       
  directive:
    type: str
    description: ' Directives tell the client how to backup certain files. For example, +compressasm: *.o tells the backup to compress all .o files at or below the invocation directory.'
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
- name: Get all directives
  dellemc.networker.directive:
    state: get

- name: Get directive by name
  dellemc.networker.directive:
    state: get
    name: NT standard directives

- name: Create directive
  dellemc.networker.directive:
    state: create
    name: VSDB Directive
    directive: |
      << /tmp >>
          skip: .?* *

- name: Modify directive
  dellemc.networker.directive:
    state: modify
    name: VSDB Directive
    directive: |
      << /tmp >>
        skip: .?* *
      << /etc >>
        skip: .?* *

- name: Delete directive
  dellemc.networker.directive:
    state: delete
    name: VSDB Directive

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
        'name': {'type': 'str'},
        'comment': {'type': 'str'},
        'directive': {'type': 'str'},
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
    api_initialize = DirectivesApi(auth=auth, url=url)

    if state == 'get':
        if module.params['name'] is not None:
            if len(module.params['name']) > 0:
                directive_name = module.params['name']
                response = api_initialize.get_directive(directive_id=directive_name, field_params=module.params['field_params'])
                resp_msg['responses'].append(response)
        else:
            response = api_initialize.get_directives(query_params=module.params['query_params'],
                                                     field_params=module.params['field_params'])
            resp_msg['responses'].append(response)
    elif state == 'create':
        directive_name = module.params['name']
        body = params
        del body['state']
        response = api_initialize.post_directives(body=body)
        resp_msg['responses'].append(response)
        msg = 'Directive %s Created Successfully' % directive_name
        resp_msg['msg'].append(msg)
    elif state == 'modify':
        directive_name = module.params['name']
        body = params
        del body['state']
        response = api_initialize.put_directive(body=body, directive_id=directive_name)
        resp_msg['responses'].append(response)
        msg = 'Directive %s modified Successfully' % directive_name
        resp_msg['msg'].append(msg)

    elif state == 'delete':
        directive_name = module.params['name']
        response = api_initialize.delete_directive(directive_id=directive_name)
        resp_msg['responses'].append(response)
        msg = 'Directive %s deleted Successfully' % directive_name
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
            api_response = response.text
        else:
            failed = True
            changed = False
            api_response = json.loads(response.text)
        i += 1
        api_responses.append(api_response)
    module.exit_json(failed=failed, msg=api_responses, changed=changed)


if __name__ == '__main__':
    main()



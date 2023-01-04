#!/usr/bin/python3
# Copyright ©️ 2022 Dell Inc. or its subsidiaries.
from __future__ import (absolute_import, division, print_function)
import urllib3
urllib3.disable_warnings()
import json
import sys

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.datadomains_api import DatadomainApi
__metaclass__ = type


DOCUMENTATION = r'''
module: datadomains
short_description: 'This module allows to work with datadomain'
description: 'Use this module to add, delete datadomain, storageunit or folders. or modify and get information about them'
version_added: '2.0.0'
options:
  state:
    type: str
    choices:
    - create, delete, modify, get, list, read
    required: true
    description: 'Use this option to specify the action.'
  aliases:
    type: list
    description: 'Data domain aliases, like IP address'
  name:
    type: str
    description: 'Data Domain system name is the unique string.'
  userName:
    type: str
    description: 'ddboost user name.'
  ddpassword:
    type: str
    no_log: false
    description: 'ddboost user password'
  managementUser:
    type: str
    description: 'Remote user name with administrative privileges to manage Data Domain system.'
  managementPassword:
    type: str
    no_log: false
    description: 'Password for Remote user name with administrative privileges '
  storageUnit:
    type: str
    description: 'Storage Unit name'
  folder:
    type: str
    description: 'Folder name to create under storage unit'
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
- name: "Adding Data domain to networker server"
  dellemc.networker.datadomain:
    state: create
    name: datadomain.hostname
    aliases: 
        - 10.0.0.3
        - datadomain
    userName: boostuser
    ddpassword: boostpassword

- name: "Creating Storage Unit to Data Domain"
  dellemc.networker.datadomain:
    state: create
    name: datadomain.hostname
    storageUnit: storageunit

- name: "Creating Folders under storage unit"
  dellemc.networker.datadomain:
    state: create
    name: datadomain.hostname
    storageUnit: storageunit
    folder: device01

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
        'state': {'type': 'str', 'choices': ['create', 'delete', 'modify', 'get', 'list', 'read'], 'required': True},
        'aliases': {'type': 'list'},
        'name': {'type': 'str'},
        'userName': {'type': 'str'},
        'ddpassword': {'type': 'str', 'no_log': False},
        'managementUser': {'type': 'str'},
        'managementPassword': {'type': 'str', 'no_log': False},
        'storageUnit': {'type': 'str'},
        'folder': {'type': 'str'},
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
    if 'ddpassword' in params:
        params['password'] = params.pop('ddpassword')
    url = f'https://{server}:{port}/nwrestapi/v3/global'
    failed, changed, msg, resp_msg = False, False, "", dict()
    resp_msg['responses'] = []
    resp_msg['msg'] = []
    api_initialize = DatadomainApi(auth=auth, url=url)

    if state == 'get':
        if module.params['name'] is not None:
            if len(module.params['name']) > 0:
                dd_name = module.params['name']
                response = api_initialize.get_data_domain_system(data_domain_system_id=dd_name,
                                                                 field_params=module.params['field_params'])
                resp_msg['responses'].append(response)
        else:
            response = api_initialize.get_data_domain_systems(field_params=module.params['field_params'],
                                                              query_params=module.params['query_params'])
            resp_msg['responses'].append(response)
    elif state == 'create':
        dd_name = module.params['name']
        response = ''
        if 'storageUnit' not in params and 'folder' not in params:
            body = params
            del body['state']
            response = api_initialize.post_data_domain(body=body)
            msg = 'Data Domain %s added successfully' % dd_name
        elif 'storageUnit' in params and 'folder' in params:
            body = params
            storageUnit = params['storageUnit']
            folder = params['folder']
            del body['state']
            del body['name']
            response = api_initialize.post_op_create_folder(body=body, data_domain_system_id=dd_name)
            msg = 'Folder %s Created Successfully under storage unit %s on data domain %s' % (folder, storageUnit, dd_name)
        elif 'storageUnit' in params and 'folder' not in params:
            body = params
            del body['state']
            del body['name']
            storageUnit = params['storageUnit']
            response = api_initialize.post_op_create_unit(body=body, data_domain_system_id=dd_name)
            msg = 'Storage unit %s Created Successfully on data domain %s' % (storageUnit, dd_name)

        resp_msg['responses'].append(response)
        resp_msg['msg'].append(msg)
    elif state == 'modify':
        dd_name = module.params['name']
        body = params
        del body['state']
        response = api_initialize.put_data_domain_system(body=body, data_domain_system_id=dd_name)
        resp_msg['responses'].append(response)
        msg = 'Protection Group %s modified Successfully' % dd_name
        resp_msg['msg'].append(msg)

    elif state == 'delete':
        dd_name = module.params['name']
        response = ''
        if 'storageUnit' not in params and 'folder' not in params:
            response = api_initialize.delete_data_domain_system(data_domain_system_id=dd_name)
            msg = 'Data Domain %s deleted successfully' % dd_name
        elif 'storageUnit' in params and 'folder' in params:
            body = params
            del body['state']
            del body['name']
            storageUnit = params['storageUnit']
            folder = params['folder']
            response = api_initialize.post_op_delete_folder(body=body, data_domain_system_id=dd_name)
            msg = 'Folder %s Deleted Successfully under storage unit %s on data domain %s' % (folder, storageUnit, dd_name)
        elif 'storageUnit' in params and 'folder' not in params:
            body = params
            del body['state']
            del body['name']
            storageUnit = params['storageUnit']
            response = api_initialize.post_op_delete_storage_unit(body=body, data_domain_system_id=dd_name)
            msg = 'Storage unit %s Deleted Successfully on data domain %s' % (storageUnit, dd_name)
        resp_msg['responses'].append(response)
        resp_msg['msg'].append(msg)

    elif state == 'list':
        dd_name = module.params['name']
        response = ''
        if 'storageUnit' in params and 'folder' in params:
            body = params
            del body['state']
            response = api_initialize.post_op_list_folders(body=body, data_domain_system_id=dd_name)
            resp_msg['responses'].append(response)
        elif 'storageUnit' in params and 'folder' not in params:
            body = params
            del body['state']
            response = api_initialize.post_op_list_units(body=body, data_domain_system_id=dd_name)
        else:
            body = {}
            response = api_initialize.post_op_list_units(body=body, data_domain_system_id=dd_name)
            resp_msg['responses'].append(response)
        resp_msg['responses'].append(response)
        resp_msg['msg'].append(msg)

    elif state == 'read':
        dd_name = module.params['name']
        response = ''
        if 'storageUnit' in params and 'folder' in params:
            body = params
            del body['state']
            response = api_initialize.post_op_read_folder(body=body, data_domain_system_id=dd_name)
            resp_msg['responses'].append(response)
        elif 'storageUnit' in params and 'folder' not in params:
            body = params
            del body['state']
            response = api_initialize.post_op_read_unit(body=body, data_domain_system_id=dd_name)
            resp_msg['responses'].append(response)
        resp_msg['responses'].append(response)
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
        elif "There is already a" in response.text or "Host name conflict found" in response.text or "already exists" in response.text:
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

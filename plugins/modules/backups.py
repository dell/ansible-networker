#!/usr/bin/python3
# Copyright ©️ 2022 Dell Inc. or its subsidiaries.
from __future__ import (absolute_import, division, print_function)
import urllib3
urllib3.disable_warnings()
import json
from ansible.module_utils.basic import AnsibleModule
from ..module_utils.backups_api import BackupsApi

__metaclass__ = type

DOCUMENTATION = r'''
module: backups
short_description: 'This module allows you to work with networker client backups'
description: 'This operation can be used to retrieve the information about all the backups. However, the query parameters can be used to filter the response.'
version_added: '2.0.0'
options:
  state:
    type: str
    choices:
    - get, delete
    required: true
    description: 'Specify the action you want to take.'
  backupId:
    type: dict
    description: 'The attribute specifies the backup id.'
  instanceId:
    type: dict
    description: 'This attribute specifies the ID of the backup instance.'
  backupMountSessionId:
    type: dict
    description: 'The value of mount session id in the Location Header attribute of a workers mount task.'
  browseSessionId:
    type: dict
    description: 'Use this attribute if you want to filter the resources as per parameter values.'    
  query_params:
    type: dict
    description: 'Use this attribute if you want to filter the resources as per parameter values.'
  field_params:
    type: list
    description: 'Use this attribute if you want to list only perticular fields'  
authors:
    - Sudarshan Kshirsagar (@kshirs1)
'''

EXAMPLES = r'''
- name: Get Alert message and priority warning.
  dellemc.networker.backup:
    state: get
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
        'state': {'type': 'str', 'choices': ['delete', 'get'], 'required': True},
        'backupId': {'type': 'str'},
        'instanceId': {'type': 'str'},
        'backupMountSessionId': {'type': 'str'},
        'browseSessionId': {'type': 'str'},
        'query_params': {'type': 'dict'},
        'field_params': {'type': 'list'},
        'dir': {'type': 'str'},
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
    url = url = f'https://{server}:{port}/nwrestapi/v3/global'
    failed, changed, msg, resp_msg = False, False, "", dict()
    resp_msg['responses'] = []
    resp_msg['msg'] = []
    api_initialize = BackupsApi(auth=auth, url=url)

    if state == 'get':
        if module.params['backupId'] is not None:
            if module.params['instanceId'] is None and module.params['backupMountSessionId'] is None and module.params['browseSessionId'] is None:
                response = api_initialize.get_backup(backup_id=module.params['backupId'])
                resp_msg['responses'].append(response)
            elif module.params['instanceId'] is not None and module.params['backupMountSessionId'] is None and module.params['browseSessionId'] is None:
                if len(module.params['instanceId']) > 0:
                    response = api_initialize.get_backup_instance(backup_id=module.params['backupId'], instance_id=module.params['instanceId'])
                    resp_msg['responses'].append(response)
                else:
                    response = api_initialize.get_backup_instances(backup_id=module.params['backupId'])
                    resp_msg['responses'].append(response)
            elif module.params['instanceId'] is None and module.params['backupMountSessionId'] is not None and module.params['browseSessionId'] is None:
                response = api_initialize.get_backup_mount_session(backup_id=module.params['backupId'],
                                                                   backup_mount_session_id=module.params['backupMountSessionId'])
                resp_msg['responses'].append(response)
            elif module.params['instanceId'] is None and module.params['backupMountSessionId'] is not None and module.params['browseSessionId'] is not None:
                response = api_initialize.get_backup_browse_session_contents(backup_id=module.params['backupId'],
                                                                   backup_mount_session_id=module.params['backupMountSessionId']
                                                                             , browse_session_id=module.params['backupMountSessionId'])
                resp_msg['responses'].append(response)

        else:
            response = api_initialize.get_backups(query_params=module.params['query_params'],
                                                 field_params=module.params['field_params'])
            resp_msg['responses'].append(response)
    elif state == 'delete':
        if module.params['backupId'] is not None:
            if module.params['sessionId'] is None and module.params['backupMountSessionId'] is None:
                response = api_initialize.delete_backup(backup_id=module.params['backupId'])
                resp_msg['responses'].append(response)
            elif module.params['sessionId'] is not None and module.params['backupMountSessionId'] is None:
                response = api_initialize.delete_backup_instance(backup_id=module.params['backupId'],
                                                                 instance_id=module.params['sessionId'])
                resp_msg['responses'].append(response)
            elif module.params['sessionId'] is None and module.params['backupMountSessionId'] is not None:
                response = api_initialize.delete_backup_mount_session(backup_id=module.params['backupId'],
                                                                      backup_mount_session_id=module.params['backupMountSessionId'])
                resp_msg['responses'].append(response)
    elif state == 'create':
        body = params
        del body['state']
        del body['backupId']
        if module.params['backupId'] is not None:
            if module.params['backupMountSessionId'] is None:
                body['hostname'] = server
                response = api_initialize.post_backup_op_mount(backup_id=module.params['backupId'], body=body)
                resp_msg['responses'].append(response)
            else:
                del body['backupMountSessionId']
                response = api_initialize.post_backup_browse_session_request(backup_id=module.params['backupId'],
                                                                             body=body,
                                                                             backup_mount_session_id=module.params['backupMountSessionId'])
                resp_msg['responses'].append(response)
    elif state == 'modify':
        body = params
        if module.params['backupId'] is not None:
            del body['state']
            del body['backupId']
            response = api_initialize.put_backup(backup_id=module.params['backupId'], body=body)
            resp_msg['responses'].append(response)

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



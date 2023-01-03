#!/usr/bin/python3
# Copyright ©️ 2022 Dell Inc. or its subsidiaries.
from __future__ import (absolute_import, division, print_function)
import urllib3
urllib3.disable_warnings()
import json
import sys
from ansible.module_utils.basic import AnsibleModule
sys.path.insert(0, '/opt/collections/dellemc/networker/')
from plugins.module_utils.recovers_api import RecoversApi
__metaclass__ = type


DOCUMENTATION = r'''
module: recovers
short_description: 'This module used to perform saveset recovery'
description: 'This module used to perform saveset recovery. The granular level recovery is not supported'
version_added: '3.0.0'
options:
  state:
    type: str
    choices:
    - create, delete, create, get
    required: true
    description: 'Choose the action you want to use'
  recoveryId:
    type: str
    description: 'is the value of the id attribute of the recover resources resourceId.'
  recoveryType:
    type: str
    choices:
    - Filesystem, BBB, NDMP, VM File Level Recover
    description: 'This attribute specifies the type of recovery.'
  recoveryDestination:
    type: str
    description: 'This attribute specifies the destination location to which the recovery is performed, as the directory pathname of the file system, NDMP backup, or block based backup.'
  itemsToRecover:
    type: list
    description: 'This attribute specifies the list of items to be recovered. For a file system, NDMP backup, or block based backup, specifies the list of full file pathnames.'
  destinationClientResID:
    type: str
    description: 'This attribute specifies the destination client ID of the remote machine to direct the recovery. The client ID can be obtained from URI /global/clients. If destination client ID is not provided, the client information from the backup instance is considered for recovery.'
  backupInstance:
    type: dict
    description: 'This attribute specifies the backup instance ID and optional clone ID to identify the backup for recovery.'
    suboptions:
      backupID:
        type: str
        description: 'This attribute specifies the instance backup ID, as either a long ID or short ID. For the HTTP-POST request, the instance backup ID can be retrieved from URI /global/backups.'
      instanceID:
        type: str
        description: 'This attribute specifies the instance ID. For the HTTP-POST request, the instance ID can be retrieved from URI /global/backups.'
  correlateBackupInstances:
    type: list
    description: 'This attribute specifies the list of items associated to "backupInstance" such as for PSS enabled NetWorker client.'
  timeStampBasedGranularRecover:
    type: dict
    description: 'This attribute specifies the source client resource ID and timestamp to identify the backup for recovery.'
    suboptions:
      sourceClientResID:
        type: str
        description: 'This attribute specifies the resource ID to uniquely identify the source client.'
      timeStamp:
        type: str
        description: 'This attribute specifies the backup savetime in the format yyyy-mm-ddThh:mm:ssXXX (2017-10-07T21:00:13+05:30) or in epoch time format (1507237222).'
  actionForDuplicateItems:
    type: str
    choices:
    - Rename, Overwrite, Skip, OverwriteFailsAction
    description: 'This attribute specifies the action to perform during recovery of the files that are already present at the recovery location.'
  targetVolume:
    type: str
    description: 'This attribute specifies the target volume to use for the image level recovery of block based backups.'
  NDMPOptions:
    type: dict
    description: 'This attribute specifies NDMP recovery options. This attribute is supported for NDMP recovery only.'
    suboptions:
      verifyIndexDB:
        type: str
        description: 'This attribute specifies whether to verify the existence of files in the index database. By default, the files are verified in the index database prior to recovery.'
      useIPv4:
        type: str
        description: 'This attribute specifies to use the IPv4 addresses for the NDMP data connection during recovery.'
  query_params:
    type: dict
    description: 'query parameters to filter the output'
  field_params:
    type: list
    description: 'Specify fields to show'
auther: 
    Sudarshan Kshirsagar (@kshirs1)
'''

EXAMPLES = r'''
- name: Get all recovers
  dellemc.networker.recovers:
    state: get

- name: Get recovery using recover ID
  recover:
    state: get
    id: 103.0.239.67.0.0.0.0.200.87.158.97.100.79.16.38

- name: recover Backup
  recover:
    state: create
    recoveryType: Filesystem
    recoveryDestination: /tmp
    backupInstance:
      backupID: bc30e742-00000006-53b3bb66-61b3bb66-00af5000-a18d9056
      instanceID: 1639168870
    actionForDuplicateItems: Rename
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
        'state': {'type': 'str', 'choices': ['create', 'delete', 'get'], 'required': True},
        'recoveryId': {'type': 'str'},
        'recoveryType': {'type': 'str', 'choices': ["Filesystem", "BBB", "NDMP", "VM File Level Recover"]},
        'recoveryDestination': {'type': 'str'},
        'itemsToRecover': {'type': 'list'},
        'destinationClientResID': {'type': 'dict'},
        'backupInstance': {'type': 'dict', 'options': {'backupID': {'type': 'str'}, 'instanceID': {'type': 'str'}}},
        'correlateBackupInstances': {'type': 'list'},
        'timeStampBasedGranularRecover': {'type': 'dict',
                                   'options': {'sourceClientResID': {'type': 'str'}, 'timeStamp': {'type': 'str'}}},
        'actionForDuplicateItems': {'type': 'str', 'choices': ["Rename", 'Overwrite', 'Skip','OverwriteFailsAction']},
        'targetVolume': {'type': 'str'},
        'NDMPOptions': {'type': 'dict', 'options': {'verifyIndexDB': {'type': 'str'}, 'useIPv4': {'type': 'str'}}},
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
    api_initialize = RecoversApi(auth=auth, url=url)

    if state == 'get':
        if module.params['name'] is not None:
            if len(module.params['name']) > 0:
                recover_name = module.params['name']
                response = api_initialize.get_recover(recover_id=recover_name)
                resp_msg['responses'].append(response)
        else:
            response = api_initialize.get_recovers(query_params=module.params['query_params'], field_params=module.params['field_params'])
            resp_msg['responses'].append(response)
    elif state == 'create':
        recover_name = module.params['name']
        body = params
        del body['state']
        response = api_initialize.post_recover(body=body)
        resp_msg['responses'].append(response)
        msg = 'recover %s Created Successfully' % recover_name
        resp_msg['msg'].append(msg)

    elif state == 'delete':
        recover_name = module.params['name']
        response = api_initialize.delete_recover(recover_id=recover_name)
        resp_msg['responses'].append(response)
        msg = 'recover %s deleted Successfully' % recover_name
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



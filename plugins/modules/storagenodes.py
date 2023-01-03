#!/usr/bin/python3
# Copyright ©️ 2022 Dell Inc. or its subsidiaries.
from __future__ import (absolute_import, division, print_function)
import urllib3
urllib3.disable_warnings()
import json
import sys

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.storagenodes_api import StorageNodesApi
__metaclass__ = type


DOCUMENTATION = r'''
module: storagenodes
short_description: ''
description: ''
version_added: ''
options:
  state:
    type: str
    choices:
    - create, delete, modify, get
    required: true
    description: 'Use this to specify action you want to take'
  comment:
    type: str
    description: 'Any user defined description of this storage node or other explanatory remarks.'
  name:
    type: str
    description: 'This attribute is the hostname of the NSR Storage Node'
  aftdAllowedDirectories:
    type: list
    description: 'AFTD supports the directory pathnames of advanced file type devices. For example: /aftd01/ (UNIX) or C:\\aftd01 (Windows)'
  cloneStorageNodes:
    type: list
    description: ' This attribute specifies the hostnames of the storage nodes that are to be selected for the "save" side of clone operations. Cloned data originating from this storage node will be directed to the first storage node that has an enabled device and a functional media daemon (nsrmmd). There is no default value. If this attribute has no value, then the "storage nodes" attribute of the client resource will be used. If that attribute has no value, then the server (nsrserverhost) is used to select a target node for the clone.'
  dedicatedStorageNode:
    type: bool
    description: 'This attribute identifies a dedicated storage node. A dedicated storage node can only backup its local data.'
  deviceSharingMode:
    type: str
    choices:
    - NoSharing, MaximalSharing, ServerDefault
    description: 'Device sharing mode at the storage node level; this is the initial value queried during device configuration. Refer to man page "nsr_storage_node_resource"'
  dynamicNsrmmds:
    type: bool
    description: ' Indicates whether additional nsrmmd processes can be started on demand to balance the load to a disk device.'
  remoteUserPassword:
    type: str
    no_log: false
    description: 'The password for the user name used to connect to the NDMP tape library server.'
  remoteUser:
    type: str
    description: 'The user name used to connect to the NDMP tape library server.'
  searchAllLuns:
    type: bool
    description: 'Set to "Yes" if you want NetWorker to search all the luns for every SCSI target. Setting it to "Yes" may make device detection take a very long time to complete. Setting it to "No" makes NetWorker stop searching at the first unused lun for a target.'
  sharedDeviceCreation:
    type: bool
    description: 'Set to "Yes" if you wish to allow Restricted Data Zone users to be able to create new devices or jukeboxes on the storage node if the storage node is shared. A storage node is considered shared if it has no Restricted Data Zone associations.'
  skipScsiTargets:
    type: bool
    description: 'This attribute contains the scsi targets that need to be skipped by the auto-detect process. The targets are in the form "bus.target.lun", where the target and lun fields are optional. When specifying multiple addresses, please enter one address per line. A maximum of 63 targets can be excluded.'
  skipScsiTargetAdresses:
    type: list
    description: 'Type the SCSI Address to skip'
  typeOfStorageNode:
    type: str
    description: 'The type of this storage node (SCSI, NDMP, SILO)'
    choices: 
    - SCSI, NDMP, SILO
  usePersistentNames:
    type: bool
    description: 'Set to "Yes" if you want NetWorker to use OS specific persistent device names when doing device discovery and autoconfiguration.'
  enabled:
    type: bool
    description: 'This attribute indicates whether the storage node is available for use. The service mode stops new commands from being submitted to run any devices on this storage node, while allowing existing commands to cancel. Note that when service mode is selected, nsrd will automatically change the state to disabled after all outstanding commands on devices on the jukebox have been cancelled.'
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
        'aftdAllowedDirectories': {'type': 'list'},
        'cloneStorageNodes': {'type': 'list'},
        'dedicatedStorageNode': {'type': 'bool'},
        'deviceSharingMode': {'type': 'str', 'choices': ['NoSharing', 'MaximalSharing', 'ServerDefault']},
        'dynamicNsrmmds': {'type': 'bool'},
        'remoteUserPassword': {'type': 'str', 'no_log': False},
        'remoteUser': {'type': 'str'},
        'searchAllLuns': {'type': 'bool'},
        'sharedDeviceCreation': {'type': 'bool'},
        'skipScsiTargets': {'type': 'bool'},
        'skipScsiTargetAdresses': {'type': 'list'},
        'typeOfStorageNode': {'type': 'str', 'choices': ['SCSI', 'NDMP', 'SILO']},
        'usePersistentNames': {'type': 'bool'},
        'enabled': {'type': 'bool'},
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
    api_initialize = StorageNodesApi(auth=auth, url=url)
    module.params['password'] = module.params.pop('remoteUserPassword')
    if state == 'get':
        if module.params['name'] is not None:
            if len(module.params['name']) > 0:
                storagenode_name = module.params['name']
                response = api_initialize.get_storagenode(storagenode_id=storagenode_name, field_params=module.params['field_params'])
                resp_msg['responses'].append(response)
        else:
            response = api_initialize.get_storagenodes(field_params=module.params['field_params'], query_params=module.params['query_params'])
            resp_msg['responses'].append(response)
    elif state == 'create':
        storagenode_name = module.params['name']
        body = params
        del body['state']
        response = api_initialize.post_storagenode(body=body)
        resp_msg['responses'].append(response)
        msg = 'Storage Node %s Created Successfully' % storagenode_name
        resp_msg['msg'].append(msg)
    elif state == 'modify':
        storagenode_name = module.params['name']
        body = params
        del body['state']
        response = api_initialize.put_storagenode(body=body, storagenode_id=storagenode_name)
        resp_msg['responses'].append(response)
        msg = 'Storage Node %s modified Successfully' % storagenode_name
        resp_msg['msg'].append(msg)

    elif state == 'delete':
        storagenode_name = module.params['name']
        response = api_initialize.delete_storagenode(storagenode_id=storagenode_name)
        resp_msg['responses'].append(response)
        msg = 'Storage Node %s deleted Successfully' % storagenode_name
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



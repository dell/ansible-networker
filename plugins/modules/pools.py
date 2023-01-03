#!/usr/bin/python3
# Copyright ©️ 2022 Dell Inc. or its subsidiaries.
from __future__ import (absolute_import, division, print_function)
import urllib3
urllib3.disable_warnings()
import json
import sys

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.pools_api import PoolsApi
__metaclass__ = type


DOCUMENTATION = r'''
module: pools
short_description: 'This module allows to work with NetWorker Media Pools'
description: 'Use this module to Create, delete, modify media pools or get information about media pools'
version_added: '2.0.0'
options:
  state:
    type: str
    choices:
    - create, delete, modify, get
    required: true
    description: 'Use this field to specify the action to take on media pool.'
  autoMediaVerify:
    type: bool
    description: 'Determines whether or not automated verification is performed while data is being written to a volume from this pool.'
  barcodePrefix:
    type: str
    description: 'Only barcodes with this prefix are selected for this pool.'
  comment:
    type: str
    description: 'Any user defined description of this pool or other explanatory remarks.'
  createDltWorm:
    type: bool
    description: 'his attribute indicates whether any tapes labelled in this WORM pool should be initialized as DLTWORM tapes, assuming that they are in DLTWORM capable drives. In non-WORM pools or drives that are not DLTWORM capable it will have no effect.'
  devices:
    type: list
    description: 'The devices that volumes are allowed to be mounted onto.'
  enabled:
    type: bool
    description: 'Determines whether this pool should be considered for selection'
  labelTemplate:
    type: str
    description: 'The template that is to be used when labeling volumes in this pool.'
  maxParallelism:
    type: int
    description: 'Limits the number of parallel sessions per device allowed when saving to this pool.'
  maxVolumesToRecycle:
    type: int
    description: 'Maximum number of volumes to be recycled.'
  mediaTypeRequired:
    type: str
    description: ' If specified, the media type required attribute enforces that only media of this type can be labeled into this pool. This attribute cannot be set if the media type preference attribute is set. This attribute cannot be used to specify the capacity of the media.'
  mediaTypePreferred:
    type: str
    description: ' If specified, the media type preference attribute is used as a selection factor when a request is made for a writable volume. The preferred type will be considered first within a priority level (jukebox/stand alone device). This attribute cannot be set if the media type required attribute is set.This attribute cannot be used to specify the capacity of the media.'
  name:
    type: str
    description: 'The name of the pool'
  poolType:
    type: str
    choices:
    - Backup, ArchiveClone, Archive, BackupClone
    description: 'Determines how volumes that are members of this pool will be used.'
  recycleFromOtherPools:
    type: bool
    description: ' Determines whether pool can recycle volumes from other pools.'
  recycleInterval:
    type: str
    description: 'The interval time specifies how often recycling runs. The default value is 24:00, which means run once a day.'
  recycleStart:
    type: str
    description: 'Time to start recycling (HH:MM).'
  recycleStartNow:
    type: bool
    description: ''
  recycleToOtherPools:
    type: bool
    description: 'Determines whether recyclable volumes can be used by other pools.'
  storeIndexEntries:
    type: bool
    description: 'Determines whether or not file index entries are generated for this pool.'
  volumeTypePreference:
    type: str
    description: ''
  wormPool:
    type: bool
    description: 'This attribute indicates whether the pool will use WORM tapes (and only WORM tapes). Only tape drives that are WORM capable can be assigned to WORM pools.'
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
- name: Creating pools Templates
  dellemc.networker.pool:
    state: create
    name: BackupVolumes
    enabled: yes
    labelTemplate: BackupVolumesLabel
    poolType: Backup
    mediaTypeRequired: Data Domain
    storeIndexEntries: yes
    devices:
        - dev01
        - dev02
        
- name: Modifying pools Templates
  dellemc.networker.pool:
    state: modify
    name: BackupVolumes
    devices:
        - dev01
        - dev02
        - dev03

- name: Deleting pools Templates
  dellemc.networker.pool:
    state: delete
    name: BackupVolumes    

- name: Get pools Templates
  dellemc.networker.pool:
    state: get
    name: BackupVolumes       
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
        'autoMediaVerify': {'type': 'bool'},
        'barcodePrefix': {'type': 'str'},
        'comment': {'type': 'str'},
        'createDltWorm': {'type': 'bool'},
        'devices': {'type': 'list'},
        'enabled': {'type': 'bool'},
        'labelTemplate': {'type': 'str'},
        'maxParallelism': {'type': 'int'},
        'maxVolumesToRecycle': {'type': 'int'},
        'mediaTypeRequired': {'type': 'str'},
        'mediaTypePreferred': {'type': 'str'},
        'name': {'type': 'str'},
        'poolType': {'type': 'str', 'choices': ['Backup', 'ArchiveClone', 'Archive', 'BackupClone']},
        'recycleFromOtherPools': {'type': 'bool'},
        'recycleInterval': {'type': 'str'},
        'recycleStart': {'type': 'str'},
        'recycleStartNow': {'type': 'bool'},
        'recycleToOtherPools': {'type': 'bool'},
        'storeIndexEntries': {'type': 'bool'},
        'volumeTypePreference': {'type': 'str'},
        'wormPool': {'type': 'bool'},
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
    api_initialize = PoolsApi(auth=auth, url=url)

    if state == 'get':
        if module.params['name'] is not None:
            if len(module.params['name']) > 0:
                pool_name = module.params['name']
                response = api_initialize.get_pool(pool_id=pool_name, field_params=module.params['field_params'])
                resp_msg['responses'].append(response)
        else:
            response = api_initialize.get_pools(field_params=module.params['field_params'],
                                                query_params=module.params['query_params'])
            resp_msg['responses'].append(response)
    elif state == 'create':
        pool_name = module.params['name']
        body = params
        del body['state']
        response = api_initialize.post_pool(body=body)
        resp_msg['responses'].append(response)
        msg = 'Protection Group %s Created Successfully' % pool_name
        resp_msg['msg'].append(msg)
    elif state == 'modify':
        pool_name = module.params['name']
        body = params
        del body['state']
        response = api_initialize.put_pool(body=body, pool_id=pool_name)
        resp_msg['responses'].append(response)
        msg = 'Protection Group %s modified Successfully' % pool_name
        resp_msg['msg'].append(msg)

    elif state == 'delete':
        pool_name = module.params['name']
        response = api_initialize.delete_pool(pool_id=pool_name)
        resp_msg['responses'].append(response)
        msg = 'Protection Group %s deleted Successfully' % pool_name
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



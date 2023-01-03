#!/usr/bin/python3
# Copyright ©️ 2022 Dell Inc. or its subsidiaries.
from __future__ import (absolute_import, division, print_function)
import urllib3
urllib3.disable_warnings()
import json
import sys

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.devices_api import DevicesApi

__metaclass__ = type


DOCUMENTATION = r'''
module: devices
short_description: 'This module allows to work with NetWorker devices'
description: 'Use this module to Create, delete, modify Protection devices or get information about them'
version_added: '2.0.0'
options:
  state:
    type: str
    choices:
    - create, delete, modify, get, label, mount, unmount, erase, verify_label
    required: true
    description: 'Use this to specify the action you want to take.'
  comment:
    type: str
    description: 'Any user defined description of this device or other explanatory remarks.'
  name:
    type: str
    description: "The name of the device that the server uses to save and recover data. The device name is usually the path name of a tape or a file type device such as /dev/nrmt8. The name may be prefixed with ''rd='', the devices hostname and a colon. For an adv_file or Data Domain device the name can be any string. For an adv_file or Data Domain device use the ''device access infomation'' attribute to specify a path. The name cannot be changed once the device is created - use delete and create a new device if necessary."
  deviceAccessInfo:
    type: str
    description: 'The device access information attribute specifies the access path for an advance file or a Data Domain device. The access information string must have one of the following formats: <host name>:<device path> or <device path> depending on the device type. For Data Domain devices, <host name> is the host name of the Data Domain server and <device path> is the path relative to the mount point exported by the Data Domain server. The Data Domain device path should begin with the short host name of the NetWorker server. For an NFS-based advanced file device, <host name> is the host name of the NFS server and <device path> is the full exported path to the desired directory. For other advanced file devices, <device path> is an absolute client-accessible path to the device (use of UNC or automounter paths is recommended). For these devices, the first value in this list must be an absolute path to the device on the storage node on which the device is defined'
  mediaType:
    type: str
    description: 'The media type describes the actual storage media. The list of possible selections is quite extensive. See the NetWorker Administrators Guide for more details. Note, the media type cannot be changed once the device has been created.'
  remoteUser:
    type: str
    description: "The username is used to connect to the NDMP tape server, Data Domain server, or the UNC or NFS adv_file device path on a network drive. For CloudBoost devices, this is the 'token-id' or 'access key' supplied by the CloudBoost vendor. For NFS AFTD access, the user ID number may be appended using a colon."
  ddpassword:
    type: str
    no_log: false
    description: " The password for the username is used to connect to the NDMP tape server, Data Domain server, or the UNC adv_file device path on a network drive. For CloudBoost devices, this is the 'shared secret' or 'secret key'."
  volumePool:
    type: str
    description: 'Media Pool name to mount the device'
  writeEnabled:
    type: bool
    description: 'Use this option to specify if its write enabled or not'
  labelWithoutMount:
    type: bool
    description: 'If you want to label the device but do not mount use this option.'
  pool:
    type: str
    description: 'Media pool name to mount the device'
  volume:
    type: str
    description: 'Volume Name'
  autoMediaManagement:
    type: bool
    description: 'Use this option to toggle t he auto media management'
  maxSession:
    type: str
    description: ' This attribute specifies the maximum number of save sessions for the device. It is recommended to use the default value for max sessions. A lower value can impact performance. For AFTD, the default value is 4 for target sessions and 32 for max sessions. The sessions value must be between 1 and 1024, inclusive. For CloudBoost, the default value is 10 for target sessions and 80 for max sessions. The sessions value must be between 1 and 200, inclusive. For tape, the default value is 4 for target sessions and 32 for max sessions. The sessions value must be between 1 and 512, inclusive. For ProtectPoint/DD Cloud Tier, the default value is 20 for target sessions and 60 for max sessions. The sessions value must be between 1 and 120, inclusive. For Data Domain, the default value is 20 for target sessions and 60 for max sessions. The sessions value must be between 1 and 60, inclusive.'
  readOnly:
    type: bool
    description: 'Use this option if you want to mark the device as read only.'
  status:
    type: str
    choices:
    - Enabled, Disabled
    description: 'Enable or disable the device.'
  targetSession:
    type: str
    description: ' This attribute specifies the number of save sessions dispatched to this device before another device is considered.'
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
- name: Create Devices
  device:
    state: create
    name: dev01
    deviceAccessInfo: ddhostname01:/storageUnit/device01"
    mediaType: "Data Domain"
    remoteUser: "boostuser"
    volumePool: "BackupVolumes"
    ddpassword: "password01"


- name: Label Devices
  device:
    state: label
    name: dev01
    labelWithoutMount: false
    pool: BackupVolumes

- name: Label Devices
  device:
    state: label
    name: dev01
    labelWithoutMount: false
    pool: BackupVolumes
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
        'state': {'type': 'str', 'choices': ['create', 'delete', 'modify', 'get',
                                             'label', 'mount', 'unmount', 'erase', 'verify_label'], 'required': True},
        'comment': {'type': 'str'},
        'name': {'type': 'str'},
        'deviceAccessInfo': {'type': 'str'},
        'mediaType': {'type': 'str'},
        'remoteUser': {'type': 'str'},
        'ddpassword': {'type': 'str', 'no_log': False},
        "volumePool": {'type': 'str'},
        'writeEnabled': {'type': 'bool'},
        'labelWithoutMount': {'type': 'bool'},
        'pool': {'type': 'str'},
        'volume': {'type': 'str'},
        'autoMediaManagement': {'type': 'bool'},
        'maxSession': {'type': 'str'},
        'readOnly': {'type': 'bool'},
        'status': {'type': 'str', 'choices': ['Enabled', 'Disabled']},
        'targetSession': {'type': 'str'},
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
    api_initialize = DevicesApi(auth=auth, url=url)

    if state == 'get':
        if module.params['name'] is not None:
            if len(module.params['name']) > 0:
                device_name = module.params['name']
                response = api_initialize.get_device(device_id=device_name,
                                                     field_params=module.params['field_params'])
                resp_msg['responses'].append(response)
        else:
            response = api_initialize.get_devices(field_params=module.params['field_params'],
                                                  query_params=module.params['query_params'])
            resp_msg['responses'].append(response)
    elif state == 'create':
        device_name = module.params['name']
        body = params
        del body['state']
        response = api_initialize.post_device(body=body)
        resp_msg['responses'].append(response)
        msg = 'Device %s Created Successfully' % device_name
        resp_msg['msg'].append(msg)
    elif state == 'modify':
        device_name = module.params['name']
        body = params
        del body['state']
        response = api_initialize.put_device(body=body, device_id=device_name)
        resp_msg['responses'].append(response)
        msg = 'Device %s modified Successfully' % device_name
        resp_msg['msg'].append(msg)
    elif state == 'delete':
        device_name = module.params['name']
        response = api_initialize.delete_device(device_id=device_name)
        resp_msg['responses'].append(response)
        msg = 'Device %s deleted Successfully' % device_name
        resp_msg['msg'].append(msg)
    elif state == 'erase':
        device_name = module.params['name']
        body = {}
        response = api_initialize.post_device_op_erase(body=body, device_id=device_name)
        resp_msg['responses'].append(response)
        msg = 'Device %s Erased Successfully' % device_name
        resp_msg['msg'].append(msg)
    elif state == 'label':
        device_name = module.params['name']
        body = params
        del body['state']
        del body['name']
        response = api_initialize.post_device_op_label(body=body, device_id=device_name)
        resp_msg['responses'].append(response)
        msg = 'Device %s Labeled Successfully' % device_name
        resp_msg['msg'].append(msg)
    elif state == 'mount':
        device_name = module.params['name']
        body = params
        del body['state']
        del body['name']
        response = api_initialize.post_device_op_mount(body=body, device_id=device_name)
        resp_msg['responses'].append(response)
        msg = 'Device %s Mounted Successfully' % device_name
        resp_msg['msg'].append(msg)
    elif state == 'unmount':
        device_name = module.params['name']
        body = {}
        response = api_initialize.post_device_op_unmount(body=body, device_id=device_name)
        resp_msg['responses'].append(response)
        msg = 'Device %s unmounted Successfully' % device_name
        resp_msg['msg'].append(msg)
    elif state == 'verify_label':
        device_name = module.params['name']
        body = {}
        response = api_initialize.post_device_op_verify_label(body=body, device_id=device_name)
        resp_msg['responses'].append(response)
        msg = 'Device %s label Varified' % device_name
        resp_msg['msg'].append(response.text)

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



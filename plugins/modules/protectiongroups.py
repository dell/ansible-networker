#!/usr/bin/python3
# Copyright ©️ 2022 Dell Inc. or its subsidiaries.
from __future__ import (absolute_import, division, print_function)
import urllib3
urllib3.disable_warnings()
import json
import sys

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.protectiongroups_api import ProtectionGroupApi

__metaclass__ = type


DOCUMENTATION = r'''
module: protectiongroups
short_description: 'This module allows to work with NetWorker Protection Groups'
description: 'Use this module to Create, delete, modify Protection Groups or get information about them'
version_added: '2.0.0'
options:
  state:
    type: str
    choices:
    - create, delete, modify, get, update
    required: true
    description: 'Use this field to specify the action to take on Protection Groups.'
  comment:
    type: str
    description: 'Any user defined description of this protection group or other explanatory remarks.'
  name:
    type: str
    description: 'Specifies the name of the group. The maximum number of characters for the name of the group is 64.  After you create a group, the Name option is read-only.'
  workItemQueries:
    type: list
    description: 'This section appears when you select Query from the Group type list. This section provides you with the ability to define criteria that NetWorker will use to create a list of save sets to clone in a clone action. You can define the following types of criteria:'
  workItemSource:
    type: str
    choices:
    - Dynamic, Static
    description: 'This value can be either static or dynamic. The static keyword specifies to protect resources specified in the work item. The dynamic keyword specifies to fetch the resources on a run time basis, based on inputs provided in the work item.'
  workItemSubType:
    type: str
    description: 'This attribute specifies the work item subtype, if any. This is applicable for VMware work item type. Valid values are VirtualMachine or VMDK. The protection group can protect data with either VMDK or VirtualMachine but not both.'
  workItemType:
    type: str
    choices:
    - Client, NASDevices, SaveSetId, VMware
    description: 'Defines the type of protection group. After you create a group, the Group type option is read-only The Group Type options are listed in choices:'
  workItems:
    type: list
    description: 'This attribute specifies the list of work items.'
  vmwareWorkItemSelection:
    type: dict
    description: 'VMware Work Items'
    suboptions:
      containerMorefs:
        type: list
        description: 'This attribute specifies the list of container Managed Object Reference IDs.'
      vCenterHostname:
        type: str
        description: 'This attribute specifies the vCenter hostname.'
      vmUuids:
        type: list
        description: 'This attribute specifies the Universal Unique Identifier (UUID) of VMs.'
      vmdks:
        type: list
        description: 'List of VMDKs'
  vmwareWorkItemExclusion:
    type: dict
    description: 'Excluding VMware Items'
    suboptions:
      containerMorefs:
        type: list
        description: 'This attribute specifies the list of container Managed Object Reference IDs.'
      vCenterHostname:
        type: str
        description: 'This attribute specifies the vCenter hostname'
      vmUuids:
        type: list
        description: 'This attribute specifies the Universal Unique Identifier (UUID) of VMs.'
      vmdks:
        type: list
        description: 'List of VMDKs'
  backupOptimization:
    type: str
    choices:
    - Capacity, Performance
    description: 'This attribute specifies whether backup optimization must be performed based on capacity or performance.'
  dynamicAssociation:
    type: bool
    description: 'This attribute enables the dynamic association.'
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
- name: Create File Full Protection Group
  dellemc.networker.protectiongroup:
    state: create
    name: Sql_Full_Mon_Incr_Daily_2000_30D
    workItemType: Client

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
        'state': {'type': 'str', 'choices': ['create', 'delete', 'modify', 'get', 'update'], 'required': True},
        'comment': {'type': 'str'},
        'name': {'type': 'str'},
        'workItemQueries': {'type': 'list'},
        'workItemSource': {'type': 'str', 'choices': ['Dynamic', 'Static']},
        'workItemSubType': {'type': 'str'},
        'workItemType': {'type': 'str', 'choices': ['Client', 'NASDevices', 'SaveSetId', 'VMware']},
        'workItems': {'type': 'list'},
        'vmwareWorkItemSelection': {'type': 'dict', 'options': {
            "containerMorefs": {'type': 'list'},
            "vCenterHostname": {'type': 'str'},
            "vmUuids": {'type': 'list'},
            "vmdks": {'type': 'list'}
        }},
        'vmwareWorkItemExclusion': {'type': 'dict', 'options': {
            "containerMorefs": {'type': 'list'},
            "vCenterHostname": {'type': 'str'},
            "vmUuids": {'type': 'list'},
            "vmdks": {'type': 'list'}
        }},
        'backupOptimization': {'type': 'str', 'choices': ['Capacity', 'Performance']},
        'dynamicAssociation': {'type': 'bool'},
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
    api_initialize = ProtectionGroupApi(auth=auth, url=url)

    if state == 'get':
        if module.params['name'] is not None:
            if len(module.params['name']) > 0:
                protection_group_name = module.params['name']
                response = api_initialize.get_protection_group(protectionGroupId=protection_group_name, field_params=module.params['field_params'])
                resp_msg['responses'].append(response)
        else:
            response = api_initialize.get_protection_groups(field_params=module.params['field_params'],
                                                            query_params=module.params['query_params'])
            resp_msg['responses'].append(response)
    elif state == 'create':
        protection_group_name = module.params['name']
        body = params
        del body['state']
        response = api_initialize.post_protection_groups(body=body)
        resp_msg['responses'].append(response)
        msg = 'Protection Group %s Created Successfully' % protection_group_name
        resp_msg['msg'].append(msg)
    elif state == 'modify':
        protection_group_name = module.params['name']
        body = params
        del body['state']
        response = api_initialize.put_protection_groups(body=body, protectionGroupId=protection_group_name)
        resp_msg['responses'].append(response)
        msg = 'Protection Group %s modified Successfully' % protection_group_name
        resp_msg['msg'].append(msg)

    elif state == 'delete':
        protection_group_name = module.params['name']
        response = api_initialize.delete_protection_group(protectionGroupId=protection_group_name)
        resp_msg['responses'].append(response)
        msg = 'Protection Group %s deleted Successfully' % protection_group_name
        resp_msg['msg'].append(msg)

    elif state == 'update':
        protection_group_name = module.params['name']
        body = params
        del body['state']
        response = api_initialize.update_v_mware_work_items(body=body, protectionGroupId=protection_group_name)
        resp_msg['responses'].append(response)
        msg = 'Protection Group %s deleted Successfully' % protection_group_name
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
        elif "already exists" in response.text:
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



#!/usr/bin/python3
# Copyright ©️ 2022 Dell Inc. or its subsidiaries.
from __future__ import (absolute_import, division, print_function)
import urllib3

urllib3.disable_warnings()
import json
import sys
from ansible.module_utils.basic import AnsibleModule
from ..module_utils.schedules_api import schedulesApi

__metaclass__ = type

DOCUMENTATION = r'''
module: schedules
short_description: 'This module allows you to work with networker schedules'
description: 'Use this module to create, delete, modify schedules on networker server'
version_added: '2.0.0'
options:
  state:
    type: str
    choices:
    - create, delete, modify, get
    required: true
    description: 'Specify the action you want to take. e.g for creating schedule, use create'
  name: 
    type: str
    description: 'Name of the schedule resource'
  comment:
    type: str
    description: 'Any user defined description of this schedule'
  action:
    type: str
    description: ' This command is executed in response to the event types and priorities given, with the message on standard input.'
  additionalEmailRecipient:
    type: str
    description: 'specifies one or more email addresses of the intended recipients to be posted on occurrence of the events defined in the schedule. Use a comma to separate multiple email addresses.'
  enabled:
    type: bool
    description: 'The user as which to run remote management commands on this NAS device.'
  events:
    type: list
    description: 'A list of the events for which the given action should be taken. See the NetWorker Administrators Guide for more details. The current acceptable events are [Media, TaskManager, ResourceFile, ProtectionPolicy, DeviceCleaningRequired, Policy, CleaningCartridgeExpired, NetWorkerDaemons, BusDeviceReset, MediaCapacity, DeviceDisabled2, Server, RMAN, Client, VolumeScanNeeded, DataDomain, AdvFile, LicenseExpiration, CleaningCartridgeRequired, Index, Hypervisor, WriteCompletion, StorageNode, ProtectionPolicyFailure, Recover, DeviceCleaned, Registration, MediaRequest, DeviceOrderingIssueDetect, DeviceDisabled, DeletedMedia]'
  priorities:
    type: list
    description: 'This attribute lists the priorities at which this action should be taken. Acceptable vaules [Emergency, Notice, Warning, Waiting, Info, Critical, Alert]'
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
- name: Get all schedules
  dellemc.networker.schedules:
    state: get

- name: Create schedules
  schedule:
    state: create
    name: nsrd_issues
    action: /bin/mail -s \"backupserver's volume scan needed\" root
    events:
      - NetWorkerDaemons
    priorities:
      - Warning
      - Critical
      - Alert
      - Emergency

- name: modify schedules
  schedule:
    state: modify
    name: nsrd_issues
    action: /bin/mail -s \"backupserver's nsrd Issues detected\" root

- name: delete schedule
  dellemc.networker.schedules:
    state: delete
    name: nsrd_issues

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
        'state': {'type': 'str', 'choices': ['create', 'delete', 'modify', 'get', 'getAssociatedPolicies'], 'required': True},
        'comment': {'type': 'str'},
        'name': {'type': 'str'},
        'action': {'type': 'str'},
        'additionalEmailRecipient': {'type': 'str'},
        'enabled': {'type': 'bool'},
        'events': {'type': 'list'},
        'priorities': {'type': 'list'},
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
    api_initialize = schedulesApi(auth=auth, url=url)

    if state == 'get':
        if module.params['name'] is not None:
            if len(module.params['name']) > 0:
                schedule_name = module.params['name']
                response = api_initialize.get_schedule(schedule_id=schedule_name)
                resp_msg['responses'].append(response)
        else:
            response = api_initialize.get_schedules(query_params=module.params['query_params'],
                                                        field_params=module.params['field_params'])
            resp_msg['responses'].append(response)
    elif state == 'getAssociatedPolicies':
        if module.params['name'] is not None:
            if len(module.params['name']) > 0:
                schedule_name = module.params['name']
                response = api_initialize.get_associated_policies(schedule_id=schedule_name)
                resp_msg['responses'].append(response)

    elif state == 'create':
        schedule_name = module.params['name']
        body = params
        del body['state']
        response = api_initialize.post_schedule(body=body)
        resp_msg['responses'].append(response)
        msg = 'schedule %s Created Successfully' % schedule_name
        resp_msg['msg'].append(msg)
    elif state == 'modify':
        schedule_name = module.params['name']
        body = params
        del body['state']
        response = api_initialize.put_schedule(body=body, schedule_id=schedule_name)
        resp_msg['responses'].append(response)
        msg = 'schedule %s modified Successfully' % schedule_name
        resp_msg['msg'].append(msg)

    elif state == 'delete':
        schedule_name = module.params['name']
        response = api_initialize.delete_schedule(schedule_id=schedule_name)
        resp_msg['responses'].append(response)
        msg = 'schedule %s deleted Successfully' % schedule_name
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



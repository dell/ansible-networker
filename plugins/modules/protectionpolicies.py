#!/usr/bin/python3
# Copyright ©️ 2022 Dell Inc. or its subsidiaries.
from __future__ import (absolute_import, division, print_function)
import urllib3
urllib3.disable_warnings()
import json
import sys

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.protectionpolicies_api import ProtectionpoliciesApi
__metaclass__ = type

DOCUMENTATION = r'''
module: protectionpolicies
short_description: 'This module allows to work with NetWorker Protection Policies'
description: 'Use this module to Create, delete, modify Protection policies or get information about them'
version_added: '2.0.0'
options:
  state:
    type: str
    choices:
    - create, delete, modify, get
    required: true
    description: 'Use this field to specify the action to take on Protection '
  query_params:
    type: dict
    description: 'Use this attribute if you want to filter the resources as per parameter values.'
  field_params:
    type: list
    description: 'Use this attribute if you want to list only perticular fields'
  policy:
    type: dict
    description: 'Use this when you want work with the policy and/or workflows'
    suboptions:
      name:
        type: str
        description: 'Specifies the name of the policy.The maximum number of characters for the name of the policy is 64. After you create a policy, the Name option is read-only.'
      comment:
        type: str
        description: 'Specifies information about the policy resource.'
  workflow:
    type: dict
    description: 'Use this when you want work with the workflow '
    suboptions:
      name:
        type: str
        description: 'Specifies the name of the workflow. The maximum number of characters for the name of the workflow is 64. After you create a workflow, the Name remains editable, allowing the user to modify the name of the workflow'
      comment:
        type: str
        description: 'Specifies information about the workflow resource.'
      autoStartEnabled:
        type: bool
        choices:
        - True, False
        description: 'When you select this option, the actions in the workflow will start at the time specified in the Start time attribute, on the days defined in the action resource.'
      enabled:
        type: bool
        choices:
        - True, False
        description: 'When you select this option, the action is eligible to run when a policy or workflow that contains the action is started.  When you clear this selection, the action will not run when a policy or workflow that contains the action is started'
      endTime:
        type: str
        description: 'Use the spin boxes to define the last time to start a workflow in a defined interval period. For example, if the start time of the workflow is 7PM, the Interval value is 1 hour and the Interval End value is 11 PM, then the workflow automatically starts at 7PM, 8 PM, 9 PM, 10 PM, and 11 PM.'
      startTime:
        type: str
        description: 'Use the spin boxes to define the time to start the actions in the workflow. Click Reset to change the start time back to the original value. The default value is 9:00 P.M.'
      newName:
        type: str
        description: 'Use this option when you want to rename the workflow'
      protectionGroups:
        type: list
        description: 'Enables to you to select the protection group to add this workflow to.  To create a new protection group for this workflow, click on the green Add button.'
      startInterval:
        type: str
        description: 'Use the spin boxes to define how frequently to repeat the actions defined in the workflow over a 24 hour period. Click Reset to change the start time to the original value. The default value is 24 hours. When you specify an interval that is less than 24 hours, the Interval end attribute appears.'
      restartTimeWindow:
        type: str
        description: 'Select the duration of time, after the workflow fails or is canceled, during which the workflow can be restarted manually. A restart must be performed manually. When the selected time duration has elapsed, the restart is treated as a new run of the workflow. The available time duration is calculated from the start of the last incomplete workflow. The default value is 24 hours.'
      actions:
        type: list
        description: 'Specify the actions in list format. refer to the Example section to know more.'
        suboptions: 
            name: 
                description: action name
                type: str
            comment: 
                description: action comment
                type: str
            actionType: 
                description: action type
                type: str
                choices: ['backup', 'checkConnectivity', 'serverBackup', 'probe', 'clone']
            actionSubType: 
                description: action subtype
                type: str
                choices: ['traditional', 'snapshot']
            browsePeriod: 
                description: Browse Period. Need to modify retention period along with this property
                type: str
            retentionPeriod: 
                description: Retention Period. Need to modify browse period along with this property
                type: str
            ddRetentionLockTime: 
                description: Data domain retention lock
                type: str
            deleteSource: 
                description: Delete source saveset. Only for Clone action
                type: str
            sourceStorageNode: 
                description: source Storage node. Only for Clone action
                type: str
            destinationPool: 
                description: source destination Pool.
                type: str
            enableDdRetentionLock: 
                description: enable DD Retention Lock
                type: str
            clientOverride: 
                description: client Override
                type: str
                choices: ['clientCanOverride', 'clientCanNotOverride']
            destinationStorageNodes: 
                description: destination Storage Nodes
                type: str
            successThreshold: 
                description: success Threshold
                type: str
                choices: ['success', 'warning']
            concurrent: 
                description: concurrent actions
                type: bool
            customTags: 
                description: customTags
                type: str,
            enabled: 
                description: enable/disable action
                type: bool
                choices: [True, False]
            failureImpact: 
                description: what to do if failed
                type: str
                choices: ['continue', 'abortAction', 'abortWorkflow']
            hardLimit: 
                description: Hard limit for session
                type: str
            inactivityTimeoutInMin: 
                description: Inactivity timeout in mins
                type: int
            newName:
                description: rename action name
                type: str
            parallelism: 
                description: Action parallelism
                type: int 
            retries: 
                description: Number of reties
                type: int
            retryDelayInSec: 
                description: retry Delay In Sec
                type: int
            overideBackupSchedule:
                description: Schedule override
                type: str
            overrideRetentionPeriod:
                description: override Retention Period 
                type: str
            scheduleActivities: 
                description: schedule Activities
                type: list
            scheduleComment: 
                description: schedule Comment
                type: str
            scheduleOverrides:  
                description: schedule Overrides
                type: str
            schedulePeriod: 
                description: schedule Period
                type: str
                choices: [Week, Month]
            softLimit: 
                description: soft limit for action
                type: str    
auther: 
    Sudarshan Kshirsagar (@kshirs1)
'''

EXAMPLES = r'''
- name: Create FILE Protection Policy
  dellemc.networker.protectionpolicy:
    state: create
    policy:
      name: File

- name: Create Workflow under FILE Protection Policy
  dellemc.networker.protectionpolicy:
    state: create
    policy:
      name: File
    workflow:
      name: File_Full_Sun_Incr_Daily_2000_30D
      autoStartEnabled: yes
      comment: Added by Sudarshan 11/9/2021
      endTime: '20:00'
      startInterval: '24:00'
      startTime: '20:00'
      actions:
        - actionSpecificData:
            backup:
              backupSpecificData:
                traditional:
                  browsePeriod: 30 Days
                  destinationPool: ZV03-S
              clientOverride: ClientCanOverride
              destinationStorageNodes:
                - nsrserverhost
              retentionPeriod: 30 Days
          name: backup
          parallelism: 100
          scheduleActivities:
            - full
            - incr
            - incr
            - incr
            - incr
            - incr
            - incr
        - actionSpecificData:
            clone:
              browsePeriod: 30 Days
              destinationStorageNode: nsrserverhost
              retentionPeriod: 30 Days
              sourceStorageNode: nsrserverhost
              enableDDRetentionLock: false
              ddRetentionLockTime: ''
              destinationPool: ZV03-C
              deleteSource: false
          name: clone
          drivenBy: backup
          scheduleActivities:
            - exec
            - exec
            - exec
            - exec
            - exec
            - exec
            - exec

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

        'policy': {'type': 'dict', 'options': {
            'name': {'type': 'str'},
            'comment': {'type': 'str'}
        }},
        'workflow': {'type': 'dict', 'options': {
            'name': {'type': 'str'},
            'comment': {'type': 'str'},
            'autoStartEnabled': {'type': 'bool', 'choices': [True, False]},
            'enabled': {'type': 'bool', 'choices': [True, False]},
            'endTime': {'type': 'str'},
            'startTime': {'type': 'str'},
            'description': {'type': 'str'},
            'newName': {'type': 'str'},
            'protectionGroups': {'type': 'list'},
            'startInterval': {'type': 'str'},
            'restartTimeWindow': {'type': 'str'},
            'actions': {'type': 'list'}

        }},
        'query_params': {'type': 'dict'},
        'field_params': {'type': 'list'},
        'host': {'type': 'str', 'required': False},
        'port': {'type': 'int', 'default': 9090},
        'username': {'type': 'str', 'required': False},
        'password': {'type': 'str', 'no_log': False},
    }

    module = AnsibleModule(argument_spec=fields)
    server = module.params['host']
    user = module.params['username']
    port = module.params['port']
    password = module.params['password']
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
    if params['state'] == "get":
        if 'policy' in params and 'workflow' not in params:
            policy_name = params['policy']['name']
            workflow_name = None
            api_initialize = ProtectionpoliciesApi(auth=auth, url=url)
            response = api_initialize.get_policy_workflows(policy_id=policy_name,
                                                           field_params=module.params['field_params'],
                                                           query_params=module.params['query_params'])
            resp_msg['responses'].append(response)
        elif 'policy' in params and 'workflow' in params:
            policy_name = params['policy']['name']
            if len(params['workflow']['name']) > 0:
                workflow_name = params['workflow']['name']
                api_initialize = ProtectionpoliciesApi(auth=auth, url=url)
                response = api_initialize.get_policy_workflow(policy_id=policy_name, workflow_id=workflow_name,
                                                              field_params=module.params['field_params'])
                resp_msg['responses'].append(response)

        elif 'policy' not in params:
            policy_name = None
            api_initialize = ProtectionpoliciesApi(auth=auth, url=url)
            response = api_initialize.get_policies(field_params=module.params['field_params'],
                                                           query_params=module.params['query_params'])
            resp_msg['responses'].append(response)
        elif 'policy' in params:
            if len(params['policy']['name']) > 0:
                policy_name = params['policy']['name']
                api_initialize = ProtectionpoliciesApi(auth=auth, url=url)
                response = api_initialize.get_policy(policy_id=policy_name,
                                                     field_params=module.params['field_params'])
                resp_msg['responses'].append(response)
        else:
            response = ''
            resp_msg['responses'].append(response)

    elif params['state'] == "modify":
        if 'policy' in params and 'workflow' in params:
            policy_name = params['policy']['name']
            workflow_name = params['workflow']['name']
            api_initialize = ProtectionpoliciesApi(auth=auth, url=url)
            body = params['workflow']
            response = api_initialize.put_policy_workflow(policy_id=policy_name, workflow_id=workflow_name, body=body)
            msg = "Workflow %s modified successfully" % workflow_name
            resp_msg['responses'].append(response)
            resp_msg['msg'].append(msg)

        elif 'policy' in params and 'workflow' not in params:
            policy_name = params['policy']['name']
            api_initialize = ProtectionpoliciesApi(auth=auth, url=url)
            body = params['policy']
            response = api_initialize.put_policy(policy_id=policy_name, body=body)
            msg = "policy %s modified successfully" % policy_name
            resp_msg['responses'].append(response)
            resp_msg['msg'].append(msg)
        else:
            response = ''
            resp_msg['responses'].append(response)
    elif params['state'] == "create":
        if 'policy' in params and 'workflow' in params:
            policy_name = params['policy']['name']
            workflow_name = params['workflow']['name']
            api_initialize = ProtectionpoliciesApi(auth=auth, url=url)
            body = params['policy']
            response_policy = api_initialize.post_policy(body=body)
            msg = "Policy %s created successfully" % policy_name
            resp_msg['responses'].append(response_policy)
            resp_msg['msg'].append(msg)
            body = params['workflow']
            response_workflow = api_initialize.post_policy_workflow(body=body, policy_id=policy_name)
            msg = "Workflow %s created successfully" % workflow_name
            resp_msg['responses'].append(response_workflow)
            resp_msg['msg'].append(msg)

        elif 'policy' in params and 'workflow' not in params:
            policy_name = params['policy']['name']
            api_initialize = ProtectionpoliciesApi(auth=auth, url=url)
            body = params['policy']
            msg = "Policy %s created successfully" % policy_name
            response = api_initialize.post_policy(body=body)
            resp_msg['responses'].append(response)
            resp_msg['msg'].append(msg)

        else:
            response = ''
            resp_msg['responses'].append(response)

    elif params['state'] == "delete":
        if 'policy' in params and 'workflow' in params:
            policy_name = params['policy']['name']
            workflow_name = params['workflow']['name']
            api_initialize = ProtectionpoliciesApi(auth=auth, url=url)
            response = api_initialize.delete_policy_workflow(policy_id=policy_name, workflow_id=workflow_name)
            msg = "Workflow %s deleted successfully" % workflow_name
            resp_msg['responses'].append(response)
            resp_msg['msg'].append(msg)
        elif 'policy' in params and 'workflow' not in params:
            policy_name = params['policy']['name']
            api_initialize = ProtectionpoliciesApi(auth=auth, url=url)
            body = params['policy']
            msg = "Policy %s deleted successfully" % policy_name
            response = api_initialize.delete_policy(policy_id=policy_name)
            resp_msg['responses'].append(response)
            resp_msg['msg'].append(msg)
        else:
            response = ''
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
        elif "There is already a" in response.text or "Duplicate" in response.text:
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

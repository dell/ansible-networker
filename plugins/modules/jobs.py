#!/usr/bin/python3
# Copyright ©️ 2022 Dell Inc. or its subsidiaries.
from __future__ import (absolute_import, division, print_function)
import urllib3
urllib3.disable_warnings()
import json
from ansible.module_utils.basic import AnsibleModule
from ..module_utils.jobs_api import JobsApi

__metaclass__ = type

DOCUMENTATION = r'''
module: jobs
short_description: 'This module allows you to work with networker Job'
description: 'This operation can fetch the information about the specific job. The job is a generic label for performing any operations, such as savefs, save, archive, index, and recover operations. NetWorker removes the job information from the job database based on value of the jobsdb retention in hours attribute in the properties of the NetWorker server resource. The default jobsdb retention is 72 hours.'
version_added: '2.0.0'
options:
  state:
    type: str
    choices:
    - cancelJob, getJob, getJobGroup, getJobIndications, getJobLog
    required: true
    description: 'Specify the action you want to take.'
  jobId:
    type: dict
    description: 'This is the value of the id attribute in the job resource. It is a numeric value that uniquely identifies a job resource instance.'
  jobGroupId:
    type: dict
    description: 'This is the value of the id attribute in the job group resource.'
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
- name: Get All Jobs.
  dellemc.networker.job:
    state: getJob

- name: Get completed Jobs .
  dellemc.networker.job:
    state: getJob
    query_params:
      state: completed
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
        'state': {'type': 'str', 'choices': ['cancelJob', 'getJob', 'getJobGroup', 'getJobIndications', 'getJobLog'], 'required': True},
        'jobId': {'type': 'str'},
        'jobGroupId': {'type': 'str'},
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
    api_initialize = JobsApi(auth=auth, url=url)

    if state == 'getJob':
        if module.params['jobId'] is not None:
            job_id = module.params['jobId']
            response = api_initialize.get_job(job_id=job_id, field_params=module.params['field_params'])
            resp_msg['responses'].append(response)
        else:
            response = api_initialize.get_jobs(field_params=module.params['field_params'],
                                               query_params=module.params['query_params'])
            resp_msg['responses'].append(response)
    elif state == 'getJobGroup':
        if module.params['jobId'] is not None:
            job_group_id = module.params['jobGroupId']
            response = api_initialize.get_job_group(job_group_id=job_group_id, field_params=module.params['field_params'])
            resp_msg['responses'].append(response)
        else:
            response = api_initialize.get_job_groups(field_params=module.params['field_params'],
                                                     query_params=module.params['query_params'])
            resp_msg['responses'].append(response)
    elif state == 'getJobIndications':
        response = api_initialize.get_job_indications(field_params=module.params['field_params'],
                                                      query_params=module.params['query_params'])
        resp_msg['responses'].append(response)
    elif state == 'getJobLog':
        if module.params['jobId'] is not None:
            job_id = module.params['jobId']
            response = api_initialize.get_job_log(job_id=job_id, field_params=module.params['field_params'])
            resp_msg['responses'].append(response)
    elif state == 'cancelJob':
        body = params
        del body['state']
        if module.params['jobId'] is not None:
            job_id = module.params['jobId']
            response = api_initialize.post_job_op_cancel(job_id=job_id, body=body)
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
                try:
                    api_response = json.loads(api_response)
                except Exception as e:
                    api_response = api_response
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



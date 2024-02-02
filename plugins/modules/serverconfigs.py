#!/usr/bin/python3
# Copyright ©️ 2022 Dell Inc. or its subsidiaries.
from __future__ import (absolute_import, division, print_function)
import urllib3
urllib3.disable_warnings()
import json
import sys

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.server_api import ServerApi
__metaclass__ = type


DOCUMENTATION = r'''
module: serverconfigs
short_description: 'This module allows to work with NetWorker Server Properties, usergroups'
description: 'Use this module to modify NetWorker Server Properties or get information about them. Create or delete or modify the user groups or get information about them.'
version_added: '2.0.0'
options:
  state:
    type: str
    choices:
    - create, delete, modify, get
    required: true
    description: 'Use this field to specify the action to take on server properties, or usergroup'
  user-group:
    type: dict
    description: 'Use this option if you want to work with user groups'
    suboptions:
      name:
        type: str
        description: 'The name of the user group'
      comment:
        type: str
        description: 'Any user defined description of this user group or explanatory remarks'
      externalRoles:
        type: list
        description: "This field should be filled with role(s) from the enterprise's external LDAP v1.3 compliant repository. LDAP Role-groups are indicated by preceding the name by an ampersand ('&') character. Examples: &(netgroup poweruser), manager@jupiter OR role=manager,host=jupiter (i.e. role 'manager' on machine 'jupiter'-the LDAP Server), *@jupiter or host=jupiter (i.e. any ROLE on machine jupiter."
      privileges:
        type: list
        description: 'This attribute specifies the privileges that the members of this user group have.'
      users:
        type: list
        description: 'The list contains users or groups that are in this user group. Examples: sam@jupiter or user=sam,host=jupiter. (user sam on machine jupiter), *@jupiter or host=jupiter (any user on machine jupiter).'
  server-config:
    type: dict
    description: 'Use to get or modify the server configuration'
    suboptions:
      acceptNewRecoverSessions:
        type: bool
        description: ' This attribute determines whether the server will accept new recover sessions.'
      acceptNewSessions:
        type: bool
        description: ' This attribute determines whether the server will accept new save sessions.'
      aclPassthrough:
        type: bool
        description: 'Allow users to browse into directories with ACLs regardless of permissions.'
      administrators:
        type: list
        description: 'The administrator list contains users or groups that are allowed to add, delete, and update all NetWorker resources. Examples: sam@jupiter or user=sam,host=jupiter. (user sam on machine jupiter), *@jupiter or host=jupiter (any user on machine jupiter).'
      authenticationProxyPort:
        type: int
        description: 'This attribute sets the TCP port number of the NetWorker Authentication service proxy.'
      authenticationServiceDatabase:
        type: str
        description: 'This attribute specifies the location of the Authenticaiton Service database'
      authenticationServicePort:
        type: int
        description: ' This attribute sets the TCP port number of the NetWorker Authentication service'
      cityOrTown:
        type: str
        description: 'This attribute is part of the address field to which the enabler code should be mailed.'
      clpRefresh:
        type: str
        description: 'NSR CLP refresh forces any CLP license to be refreshed. It provides a way to force NetWorker to recognize the existence of the FLEXlm servers existence and the possibility of existing Update licenses and Capacitly Licenses'
      comment:
        type: str
        description: 'Any user defined description of this directive or other explanatory remarks.'
      company:
        type: str
        description: 'This attribute contains the name of the company for which the license enabler is issued.'
      contactName:
        type: str
        description: ' This attribute contains the name of the individual to contact for license enabler information.'
      country:
        type: str
        description: ' This attribute is part of the address field to which the enabler code should be mailed.'
      datazonePassPhrase:
        type: str
        description: ' This attribute is used to generate the datazone encryption key for backup and recover operations. If empty, the default pass phrase will be used.'
      deviceSharingMode:
        type: str
        description: 'Device sharing mode at the server level; used when device sharing mode is not set at storage node level. Refer to man page "nsr_storage_node_resource".'
      disableRpsClone:
        type: bool
        description: ' This attribute enables or disables the RPS implementation for clone operation'
      emailAddress:
        type: str
        description: 'This attribute is part of the information desired for printing the license enabler.'
      fax:
        type: str
        description: 'This attribute is part of the information required for printing the license enabler.'
      jobInactivityTimeout:
        type: int
        description: 'Global setting for the number of minutes since a job has been heard from, after which it will be declared inactive and will be terminated. This setting is enforced by nsrjobd and replaces environment variable NSR_UNRESPONSIVE_JOB_TIMEOUT. Unlike the group inactivity timeout which applies only to save processes maintaining connection to nsrmmd, this timeout applies to all processes throughout runtime. For example, if a save process were to hang in argument processing, group inactivity setting would never trigger its termination, however if this attribute is set, it will result in terminating such a hang process after number of minutes set in this attribute has passed. An empty string or a value of 0 indicates that no such timeout is in effect'
      jobsdbRetentionInHours:
        type: int
        description: 'Minimum time to keep jobs records in Jobs database, in hours'
      keepIncompleteBackups:
        type: bool
        description: 'This attribute determines if backup data from an incomplete/aborted CloudBoost backup must be retained for possible recovery'
      manualSaves:
        type: bool
        description: 'This attribute determines if manual saves are allowed to the server.'
      name:
        type: str
        description: 'The name of this NSR server is the same as the hostname by default.'
      nasDevicePolicyAllowed:
        type: bool
        description: 'This attribute enables Restricted Data Zone users to create and update group resources to select NAS device options.'
      parallelism:
        type: int
        description: 'The number of simultaneous save sessions supported by this server.'
      phone:
        type: str
        description: 'This attribute is part of the information required for printing the license enabler.'
      publicArchives:
        type: bool
        description: 'This attribute determines if a user can retrieve archived files that are owned by another user.'
      purchase-date:
        type: str
        description: 'This attribute is part of the information required for printing the license enabler.'
      saveSessionDistribution:
        type: str
        description: ' Sets the threshold for the save session distribution for all clients. The clients will distribute the save sessions to the next storage node in their storage node affinity lists when the overall target sessions or max sessions for all devices on the current storage node is exceeded. Max sessions is the default threshold but the value in the client save session distribution attribute overwrites the max sessions value'
      stateOrProvince:
        type: str
        description: 'This attribute is part of the address field to which the enabler code should be mailed.'
      streetAddress:
        type: str
        description: 'This attribute contains the address to which the enabler code should mailed.'
      supportEmailAddress:
        type: str
        description: ' This attribute specifies the email address of EMC Customer Support and is required for mail the home feature.'
      vmwarePolicyAllowed:
        type: bool
        description: 'This attribute enables Restricted Data Zone users to create and update group resources to select VMware options.'
      vmwsEnable:
        type: bool
        description: 'This attribute enables or disables the NetWorker VMware Web service daemon, nsrvmwsd, which is a module of VMware Integrated Data Protection.'
      vmwsPort:
        type: int
        description: 'This attribute sets the TCP port number of the NetWorker VMware Web service daemon, nsrvmwsd.'
      vmwsUserName:
        type: str
        description: 'This attribute sets the user name of the NetWorker VMware Web service. The user name comparison is case-sensitive.'
      vmwsUserPassword:
        type: str
        description: 'This attribute sets the user password of the NetWorker VMware Web service. It is recommended to change the default password for security reasons. The password comparison is case-sensitive.'
      volumePriority:
        type: str
        description: 'This attribute determines the priority used for selecting volumes to be written to while saving data. The value assigned to this attribute determines whether volumes in a jukebox, "NearLine Priority", or volumes managed by SmartMedia, "SmartMedia Priority" are considered first.'
      wormPoolsOnlyHoldWormTapes:
        type: bool
        description: 'This attribute determines if a WORM pool can hold only WORM tapes (if "Yes") or can hold any type of volume (if "No").'
      wormTapesOnlyInWormPools:
        type: bool
        description: 'This attribute determines if a WORM tape can only be labelled into a WORM pool (if "Yes") or can be labelled into any pool (if "No").'
      zipOrPostalCode:
        type: str
        description: 'This attribute is part of the address field to which the enabler code should be mailed.'
  audit-log-config:
    type: dict
    description: 'Audit log configuration.'
    suboptions:
      administrators:
        type: list
        description: ' The administrator list contains users or groups that are allowed to add, delete, and update all NetWorker resources. Examples: sam@jupiter or user=sam,host=jupiter. (user sam on machine jupiter), *@jupiter or host=jupiter (any user on machine jupiter).'
      auditLogFilePath:
        type: str
        description: ' This attribute specifies where the security audit log daemon writes the log file. The default location is the NetWorker logs directory, C:\Program Files\EMC NetWorker\nsr\logs on Windows and /nsr/logs on UNIX.'
      auditLogHostname:
        type: str
        description: 'This attribute specifies the hostname where the security audit log daemon nsrlogd runs and where the security audit log file is stored. By default, nsrlogd will run on the NetWorker server. For typical scenarios, this default configuration is the recommended configuration.'
      auditLogMaxFileSizeInMB:
        type: int
        description: ' This attribute specifies the maximum size of the security audit log file, in megabytes (MB). When this maximum is reached, the file is renamed for archival purposes and the default name is used to create a new security audit log file.'
      auditLogMaxFileVersion:
        type: int
        description: 'This attribute specifies the maximum number of archived security audit logs that are kept. When this maximum is reached, the oldest archived version is removed. When this value is zero, all versions are maintained.'
      auditLogRenderedLocale:
        type: str
        description: ' This attribute specifies the locale, or language, of the rendered security audit log file. By default, the en_US (English) locale is used.'
      auditLogRenderedService:
        type: str
        description: 'By default the security audit log is recorded only in the unrendered .raw format in the file <NetWorker_server_hostname>_sec_audit.raw. If set to local in addition to the .raw file a rendered .log file will also be created. Rendered versions can also be directed to either the Windows eventlog, or the UNIX syslog.'
      auditLogSeverity:
        type: str
        description: 'This attribute specifies the level of logging detail that each client provides to the security audit log server. When the level is set to information, information level and higher security related events are recorded in the security audit log file. When the level is set to critical, only the most severe security related events are recorded. This field also controls remote client security audit configuration. At the information, notice and warning levels nsrd broadcasts the security configuration to all clients during startup, at other levels the configuration is pulled by the client as needed, and not broadcast during nsrd startup'
      name:
        type: str
        description: ' This read-only attribute specifies the name of the file where security related audit messages are logged. The security audit log filename is in the format <NetWorker_server_hostname>_sec_audit.raw.'
  server-stats:
    type: str
    choices:
    - server-messages, server-statistics
    description: 'Use this option to see server-messages or statistics'
auther: 
    Sudarshan Kshirsagar (@kshirs1)
'''

EXAMPLES = r'''
- name: Toggle the Workflows
  dellemc.networker.serverconfigs:
    state: modify
    manualSaves: no
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
        'user-group': {'type': 'dict', 'options': {
            'name': {'type': 'str'},
            'comment': {'type': 'str'},
            'externalRoles': {'type': 'list'},
            'privileges': {'type': 'list'},
            'users': {'type': 'list'}
        }},
        'server-config': {'type': 'dict', 'options': {
            'acceptNewRecoverSessions': {'type': 'bool'},
            'acceptNewSessions': {'type': 'bool'},
            'aclPassthrough': {'type': 'bool'},
            'administrators': {'type': 'list'},
            'authenticationProxyPort': {'type': 'int'},
            'authenticationServiceDatabase': {'type': 'str'},
            'authenticationServicePort': {'type': 'int'},
            'cityOrTown': {'type': 'str'},
            'clpRefresh': {'type': 'str'},
            'comment': {'type': 'str'},
            'company': {'type': 'str'},
            'contactName': {'type': 'str'},
            'country': {'type': 'str'},
            'datazonePassPhrase': {'type': 'str'},
            'deviceSharingMode': {'type': 'str'},
            'disableRpsClone': {'type': 'bool'},
            'emailAddress': {'type': 'str'},
            'fax': {'type': 'str'},
            'jobInactivityTimeout': {'type': 'int'},
            'jobsdbRetentionInHours': {'type': 'int'},
            'keepIncompleteBackups': {'type': 'bool'},
            'manualSaves': {'type': 'bool'},
            'name': {'type': 'str'},
            'nasDevicePolicyAllowed': {'type': 'bool'},
            'parallelism': {'type': 'int'},
            'phone': {'type': 'str'},
            'publicArchives': {'type': 'bool'},
            'purchase-date': {'type': 'str'},
            'saveSessionDistribution': {'type': 'str'},
            'stateOrProvince': {'type': 'str'},
            'streetAddress': {'type': 'str'},
            'supportEmailAddress': {'type': 'str'},
            'vmwarePolicyAllowed': {'type': 'bool'},
            'vmwsEnable': {'type': 'bool'},
            'vmwsPort': {'type': 'int'},
            'vmwsUserName': {'type': 'str'},
            'vmwsUserPassword': {'type': 'str'},
            'volumePriority': {'type': 'str'},
            'wormPoolsOnlyHoldWormTapes': {'type': 'bool'},
            'wormTapesOnlyInWormPools': {'type': 'bool'},
            'zipOrPostalCode': {'type': 'str'}
        }},
        'audit-log-config': {'type': 'dict', 'options': {
            'administrators': {'type': 'list'},
            'auditLogFilePath': {'type': 'str'},
            'auditLogHostname': {'type': 'str'},
            'auditLogMaxFileSizeInMB': {'type': 'int'},
            'auditLogMaxFileVersion': {'type': 'int'},
            'auditLogRenderedLocale': {'type': 'str'},
            'auditLogRenderedService': {'type': 'str'},
            'auditLogSeverity': {'type': 'str'},
            'name': {'type': 'str'}
        }},
        'server-stats': {'type': 'str', 'choices': ['server-messages', 'server-statistics']},
        'host': {'type': 'str', 'required': True},
        'port': {'type': 'int', 'default': 9090},
        'username': {'type': 'str', 'required': True},
        'password': {'type': 'str', 'no_log': True},
    }

    module = AnsibleModule(argument_spec=fields,
                           mutually_exclusive=('user-group', 'server-config', 'audit-log-config', 'server-stats'))
    server = module.params['host']
    user = module.params['username']
    port = module.params['port']
    password = module.params['password']
    auth = (user, password)
    state = module.params['state']
    keys_to_delete = ['host', 'username', 'port', 'password']
    for key in keys_to_delete:
        if key in module.params:
            del module.params[key]
    params = remove_none(module.params)
    url = f'https://{server}:{port}/nwrestapi/v3/global'
    failed, changed, msg, resp_msg = False, False, "", dict()
    resp_msg['responses'] = []
    resp_msg['msg'] = []
    state_to_req = {'get': 'get', 'create': 'post', 'delete': 'delete', 'modify': 'put'}
    past_tense = {'create': 'creaeted', 'delete': 'deleted', 'modify': 'modified'}
    command = ''
    for key, value in params.items():
        if key != 'state':
            if isinstance(params[key], dict):
                func = '%s_%s' % (state_to_req[state], key.replace("-", "_"))
                state_to_check = ['get', 'delete']
                if state in state_to_check:
                    var = "%s_id" % key.replace("-", "")
                    if len(params[key]['name']) > 0:
                        var_value = params[key]['name']
                        command = '%s(%s="%s")' % (func, var, var_value)
                    else:
                        func = '%s_%ss' % (state_to_req[state], key.replace("-", "_"))
                        command = "%s()" % func
                    if state == 'delete':
                        var_value = params[key]['name']
                        msg = "%s %s %s successfully" % (key, var_value, past_tense[state])
                        resp_msg['msg'].append(msg)

                elif state == 'modify' and key == 'user-group':
                    body = params[key]
                    var_value = params[key]['name']
                    command = '%s(body=%s, usergroup_id="%s")' % (func, body, var_value)
                    msg = "%s %s %s successfully" % (key, var_value, past_tense[state])
                    resp_msg['msg'].append(msg)
                else:
                    body = params[key]
                    try:
                        var_value = params[key]['name']
                    except KeyError:
                        var_value = ''
                    command = '%s(body=%s)' % (func, body)
                    msg = "%s %s %s successfully" % (key, var_value, past_tense[state])
                    resp_msg['msg'].append(msg)
            else:
                func = '%s_%s' % (state_to_req[state], value.replace("-", "_"))
                command = "%s()" % func


    api_initialize = ServerApi(auth=auth, url=url)
    response = eval("api_initialize.%s" % command)
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

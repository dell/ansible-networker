#!/usr/bin/python3
# Copyright ©️ 2022 Dell Inc. or its subsidiaries.
from __future__ import (absolute_import, division, print_function)
import urllib3
urllib3.disable_warnings()
import json
import sys

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.clients_api import ClientsApi
__metaclass__ = type


DOCUMENTATION = r'''
module: clients
short_description: 'This module allows to work with clients'
description: 'Use this module to add, delete Clients or folders. or modify and get information about them'
version_added: '2.0.0'
options:
  state:
    type: str
    choices:
    - create, delete, modify, get, run_backup, get_agents, get_instances, get_indexes,
      get_backups
    required: true
    description: 'Use this option to specify action'
  agent_type:
    type: str
    choices:
    - local_agent, remote_agents
    description: 'Agent Type'
  backup_id:
    type: str
    description: 'The attribute specifies the backup id.'
  instance_id:
    type: str
    description: 'This attribute specifies the ID of the backup instance.'
  aliases:
    type: list
    description: 'This is a list of aliases (nicknames) for the client machine that queries can match. If this list is empty, match on client name alone.'
  backupCommand:
    type: str
    description: 'The remote command to run to backup data for this client and save sets. This command can be used to perform pre and post backup processing and defaults to the "save" command. The value must not include a path and must start with the prefix "save" or "nsr".'
  backupType:
    type: str
    description: 'Backup Type'
  blockBasedBackup:
    type: bool
    description: 'Select this attribute to enable the image backups. Refer to the NetWorker Administration Guide for additional information about configuring block based backups.'
  checkpointEnabled:
    type: bool
    description: 'This attribute enables the support for checkpoint restart during scheduled backups. The save program performs a backup in an ordered manner and keeps track of the files saved. If save fails, it can be restarted from the point of interruption (file or directory). The ordering of the filesystems during backup may cause performance impact.'
  clientId:
    type: str
    description: "This attribute is the client's identifier and cannot be changed."
  clientState:
    type: bool
    description: 'Client State'
  nasDevice:
    type: bool
    description: 'Indicates client is a NAS device.'
  ndmp:
    type: bool
    description: ' Indicates client is a NDMP client.'
  ndmpMultiStreamsEnabled:
    type: bool
    description: ' Indicates client is to use the NDMP multistream feature.'
  ndmpVendorInformation:
    type: list
    description: ' This attribute contains NDMP client vendor information.'
  parallelSaveStreamsPerSaveSet:
    type: bool
    description: "Parallel save streams per save set - Enable parallel save streams per client resource save set during scheduled backup. Large save set backup time could be significantly reduced. Each save set will be backed-up with four parallel save streams by default. The default four can be changed by setting the 'PSS:streams_per_ss' parameter in the clients save operations attribute. For example, 'PSS:streams_per_ss=1,*, 2,/data[1-3], 8,/data[45]' will use one stream per Unix client save set entry by default but two streams for each of /data1, /data2 & /data3 and eight streams for each of /data4 & /data5. Client-supported wildcard characters can be used. The total number of active streams from all save sets at any one point in time will not exceed the clients parallelism, which is recommended to be a multiple of the default four or the largest ''PSS:streams_per_ss'' integer value if set."
  parallelism:
    type: str
    description: 'The number of save sets to run in parallel.'
  protectionGroups:
    type: list
    description: ' The groups this client is part of for workflow runs. The choices are defined by the set of existing groups.'
  remoteAccessUsers:
    type: list
    description: "A list of remote users that are allowed to recover this client's files. If empty, only users logged into this machine are valid. Examples: sam@jupiter or user=sam,host=jupiter (user sam on machine jupiter), group=wheel,host=jupiter (any user in group wheel on host jupiter), jupiter or host=jupiter (any user on machine jupiter). Warning: If using the Restricted Data Zones feature it is possible to give access to someone not explicitly in the associated Restricted Data Zone. Use caution with wildcard characters."
  saveSets:
    type: list
    description: ' A list of the save sets to be backed up for this client with this schedule'
  scheduledBackup:
    type: bool
    description: ' This attribute indicates if this client is enabled for scheduled backup'
  storageNodes:
    type: list
    description: ' This is an ordered list of storage nodes for the client to use when saving its data. Its saves are directed to the first storage node that has an enabled device and a functional media daemon (nsrmmd). Keywords curphyhost and currechost can be used in this list only for virtual clients in a cluster. curphyhost indicates backups of a virtual client should go to the storage node on the physical host on which the virtual client resides. While currechost requests the required volume be mounted on the storage node where the recover operation is running. This list is also used during cloning; when a clone operation begins, the storage node from which the cloned data originates is consulted, and its "clone storage nodes" attribute is used, if present, as the save-side storage node. If not present, this list of storage nodes will be used to select the save-side storage node'
  virtualClient:
    type: bool
    description: ' This attribute indicates whether the client is a virtual machine'
  physicalHost:
    type: str
    description: "This attribute specifies the physical hostname, if this resource is for a virtual client. The hostname does not need to be fully-qualified, and must be less than 64 bytes. All clients sharing the same physical host must use the identical name (don't mix name formats such as short, FQDN or IP address)."
  retentionPolicy:
    type: str
    description: ' The media policy used to define the retention time for client save sets. The existing set of management policies define the choices.'
  indexHostname:
    type: str
    description: "This is the 'client entry' under which the index entries will be stored. The client entry must be created and active when the index value is set."
  fileInactivityThreshold:
    type: str
    description: 'The number of days a file has not been accessed before it is counted as inactive. A value of zero indicates that no inactivity statistics will be collected for this client.'
  fileInactivityAlertThreshold:
    type: str
    description: 'Percentage of space occupied by inactive files, exceeding which will generate a notification. A value of zero indicates that no alert will be sent for this client.'
  checkpointGranularity:
    type: str
    choices:
    - Directory, File
    description: 'Checkpoint restart by file means that checkpoint will be created after each file is backed up. Due to performance degradation, this is recommended for savesets with a few large files only. Checkpoint restart by directory guarantees that checkpoint will be created after each directory is backed up. Checkpoints may be created at intermediate points depending on the number of files in the directory; however, this is not guaranteed.'
  clientDirect:
    type: bool
    description: 'A client direct backup bypasses the storage node and writes directly to the target disk device during a scheduled backup of the client. The target disk device can be a Data Domain or an Advanced File Type (AFTD) device. When enabled, client direct is attempted on the target disk. If a client direct backup is not possible, a storage node backup is attempted. This attribute is supported on 8.0 or later clients. For pre-7.6.1 clients, leave this attribute enabled (default setting). Although client direct is not supported on pre-8.0 clients, disabling this attribute may cause the backup to fail.'
  scheduleBackup:
    type: bool
    description: 'This attribute indicates if this client is enabled for scheduled backup'
  directive:
    type: str
    description: 'Directives tell the client how to backup certain files. The choices are defined by the set of existing directives.'
  pool:
    type: str
    description: 'Media pool used for data target selection during scheduled backup of the save sets specified in this client. This attribute is supported on 7.6.1 or later clients. Backup may fail on older (pre-7.6.1) clients for non-NULL value. This pool selection overrides any other pool criteria associated with the group or save set for this client.'
  schedule:
    type: str
    description: 'The schedule this client will use for backups. The choices are defined by the set of existing schedules.'
  backupRenamedDirectories:
    type: str
    description: 'This attribute enables the support of renamed directories during scheduled backups. The save program performs a lookup in the client file index to determine whether a directory has been renamed. If a directory has been renamed, all of the files and subdirectories under the directory will be backed up.'
  remoteUser:
    type: str
    description: 'The user as which to run remote commands on this client or to use to access application specific data. Each instance of a client can have a different value for the "remote user".'
  remoteUserPassword:
    type: str
    description: ' The commands save and savefs use the password to gain access to the files being backed up, and other backup commands may use it to access application data. If a password is given, then the "remote user" attribute for the client resource must also be defined. This attribute is not used for Unix file system clients. Each instance of a client can have a different password.'
  preCommand:
    type: str
    description: 'The command that is specified here runs before the save sets for this client. The value must not include a path and must start with the prefix "save" or "nsr".'
  postCommand:
    type: str
    description: 'The command that is specified here runs after the save sets are completed for this client. The value must not include a path and must start with the prefix "save" or "nsr".'
  saveOperations:
    type: str
    description: ' Save operation instructions of the form:KEYWORD:TOKEN=STATE. This attribute is required if Save set attribute for this client contains non-ASCII names. I18N:mode=nativepath is for NetWorker 7.4 or later clients on UNIX platforms and I18N:mode=utf8path is for pre-7.4 clients and NetWorker clients on Windows platforms.'
  applicationInformation:
    type: str
    description: ' This attribute contains client application information.'
  backupConfig:
    type: str
    description: 'This attribute contains internal backup configuration data.'
  jobControl:
    type: str
    choices:
    - endOnJobEnd, endOnProcessExit, useProcessExitCode
    description: ' This attribute is intended to be used with custom backup scripts. It controls how savegrp and nsrjobd interpret end of a job and/or its status.'
  ndmpMultistreamEnabled:
    type: bool
    description: ' Indicates client is to use the NDMP multistream feature.'
  ndmpLogSuccessfulFileRecovery:
    type: bool
    description: ' Indicates logging of successfully recovered files.'
  disableIpv6:
    type: bool
    description: 'Disable IPv6 for NDMP.'
  ndmpArrayName:
    type: bool
    description: ' In NDMP NAS array configurations, the logical name assigned to the array'
  dataDomainBackup:
    type: bool
    description: 'This setting ensures that the client data will be backed up only to DD Boost devices, even if the pool selected for the backups contains a mix of other device types.'
  dataDomainInterface:
    type: str
    choices:
    - ip, fiberChannel, any
    description: ' Choose the interface over which backup to a Data Domain device will occur. This option is meaningful only when Data Domain Backup is enabled for this client.'
  probeResourceName:
    type: str
    description: 'Probe resource name.'
  proxyBackupType:
    type: str
    description: 'Proxy method used for backups.'
  proxyBackupHost:
    type: str
    description: 'The host for proxy backup of this client.'
  serverNetworkInterface:
    type: str
    description: 'The unique hostname associated with the network interface on the server to be used for saves and recovers.'
  priority:
    type: str
    description: "The backup priority of this client. Priority 1 is the highest, 1000 the lowest. Automated savegrp's will attempt to back up clients with higher priorities before clients with lower priorities. Note that this is a hint only. Savegrp has many parameters to consider, and may choose a lower priority client while trying to balance the load."
  physicalClientParallelism:
    type: bool
    description: "Override the client parallelism and use the physical client's parallelism."
  saveSessionDistribution:
    type: str
    description: 'Sets the threshold for the save session distribution. The client will distribute the save sessions to the next storage node in the storage node affinity list when the overall target sessions or max sessions of all devices on the current storage node is exceeded. The default threshold is max sessions.'
  indexPath:
    type: str
    description: " The path to the client's index directory on the server. This must be either an absolute path or NULL. If NULL, the index will reside in the 'index/clientname' subdirectory of the EMC home directory ."
  executablePath:
    type: str
    description: ' The path to the NSR executables on this client.'
  backupTargetDisks:
    type: str
    description: 'This is an ordered list of disk devices for the client to use when saving its data, without refering to the storage node lists. The options can be either adv_file or Data Domain type of devices. Note that this attribute does not apply to the client of the NetWorker server.'
  ownerNotification:
    type: str
    description: 'A notification action to send the contents of status messages to the owner/primary user of a client (e.g. savegrp completion messages).'
  centralizedLogCollection:
    type: str
    description: 'This attribute enables or disables local logs collections into the Centralized Logs Storage for this client. By default, it is enabled.'
  recoverStorageNodes:
    type: list
    description: "This is an ordered list of storage nodes for the client to use when recovering data. Data will be recovered from the first storage node that has an enabled device on which we can mount the source volume and a functional media daemon (nsrmmd). If this attribute has no value, the client's `storage nodes' will be consulted. If this attribute also has no value, then the server's 'storage nodes' attribute will be used to select a target node for the recover operation. If the volume is already mounted, the storage node where it is mounted is used. If the recover storage node and read hostname for the jukebox are specified, the 'read hostname' host will be used instead of the recover storage node host. Keyword currechost can be used in this list only for virtual clients in a cluster. It requests the required volume be mounted on the storage node where the recover operation is running."
  archiveServices:
    type: bool
    description: ' This attribute determines if archive services are available for the client.'
  allSaveSetExpired:
    type: bool
    description: "This is an internal attribute indicates if the client's state can be set to decommssioned."
  nasManagementUser:
    type: str
    description: ' The user as which to run remote management commands on this NAS device. Each instance of a client can have a different value for the "NAS management user".'
  nasManagementPassword:
    type: str
    no_log: false
    description: 'This password is used to perform management actions on a NAS device. If a password is given, then the "NAS management user" attribute for the client resource must also be defined. Each instance of a client can have a different password.'
  nasManagementName:
    type: str
    description: ' In NAS device configurations, the management name of the device.'
  nasFileAccessUser:
    type: str
    description: ' This user accesses the file services on a NAS device. Each instance of a client can have a different value for the NAS management user. This field is only used with Windows clients. This field is ignored with other client types.'
  nasFileAccessPassword:
    type: str
    description: 'This password is used to access the file services on a NAS device. If a password is specified, then the NAS file server user attribute for the client resource must also be defined. Each instance of a client can have a different password. This field is only used with Windows clients. This field is ignored with other client types.'
  indexBackupContent:
    type: bool
    description: 'Index files and directories on the snapshot.'
  tags:
    type: list
    description: 'This attribute contains tags for the clients'
  comment:
    type: str
    description: 'Any user defined description of this client or other explanatory remarks.'
  name:
    type: str
    description: 'This attribute is the hostname of the NSR client. It is recommended that you specify the fully qualified domain name (FQDN) of the host. For OS cluster hosts, type the FDQN of the virtual host. For application cluster hosts, type the FQDN of the application cluster host. For example, for an Oracle cluster, type the RAC hostname. For an Exchange IP DAG, type the DAG name. The application module administrator guides provide more information.'
  query_params:
    type: dict
    description: 'Use this attribute if you want to filter the resources as per parameter values.'
  field_params:
    type: list
    description: 'Use this attribute if you want to list only perticular fields'
  resourceId:
    type: str
    description: 'For each resource, resourceId is generated by networker server and this field is used to identify the resource when you want to modify the properities for it. Use this attribute if you want to modify the properties of resource after creation.'
auther: 
    Sudarshan Kshirsagar (@kshirs1)
'''

EXAMPLES = r'''
- name: Get Single client information
  dellemc.networker.client:
    state: get
    query_params:
        hostname: oracleserver
        
- name: Get client name and backup type of all clients.
  dellemc.networker.client:
    state: get
    field_params:
        - hostname
        - backupType
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
        'state': {'type': 'str', 'choices': ['create', 'delete', 'modify', 'get', 'run_backup',
                                             'get_agents', 'get_instances', 'get_indexes', 'get_backups'], 'required': True},
        'agent_type': {'type': 'str', 'choices': ['local_agent', 'remote_agents']},
        'backup_id': {'type': 'str'},
        'instance_id': {'type': 'str'},
        'aliases': {'type': 'list'},
        'backupCommand': {'type': 'str'},
        'backupType': {'type': 'str'},
        'blockBasedBackup': {'type': 'bool'},
        'checkpointEnabled': {'type': 'bool'},
        'clientId': {'type': 'bool'},
        'clientState': {'type': 'bool'},
        'nasDevice': {'type': 'bool'},
        'ndmp': {'type': 'bool'},
        'ndmpMultiStreamsEnabled': {'type': 'bool'},
        "ndmpVendorInformation": {'type': 'list'},
        "parallelSaveStreamsPerSaveSet": {'type': 'bool'},
        "parallelism": {'type': 'str'},
        "protectionGroups": {'type': 'list'},
        "remoteAccessUsers": {'type': 'list'},
        'saveSets': {'type': 'list'},
        'scheduledBackup': {'type': 'bool'},
        'storageNodes': {'type': 'list'},
        'virtualClient': {'type': 'bool'},
        'physicalHost': {'type': 'str'},
        'retentionPolicy': {'type': 'str'},
        'indexHostname': {'type': 'str'},
        'fileInactivityThreshold': {'type': 'str'},
        'fileInactivityAlertThreshold': {'type': 'str'},
        'checkpointGranularity': {'type': 'str', 'choices': ['Directory', 'File']},
        'clientDirect': {'type': 'bool'},
        'scheduleBackup': {'type': 'bool'},
        'directive': {'type': 'str'},
        'pool': {'type': 'str'},
        'schedule': {'type': 'str'},
        'backupRenamedDirectories': {'type': 'str'},
        'remoteUser': {'type': 'str'},
        'remoteUserPassword': {'type': 'str'},
        'preCommand': {'type': 'str'},
        'postCommand': {'type': 'str'},
        'saveOperations': {'type': 'str'},
        'applicationInformation': {'type': 'str'},
        'backupConfig': {'type': 'str'},
        'jobControl': {'type': 'str', 'choices': ['endOnJobEnd', 'endOnProcessExit', 'useProcessExitCode']},
        'ndmpMultistreamEnabled': {'type': 'bool'},
        'ndmpLogSuccessfulFileRecovery': {'type': 'bool'},
        'disableIpv6': {'type': 'bool'},
        'ndmpArrayName': {'type': 'bool'},
        'dataDomainBackup': {'type': 'bool'},
        'dataDomainInterface': {'type': 'str', 'choices': ['ip', 'fiberChannel', 'any']},
        'probeResourceName': {'type': 'str'},
        'proxyBackupType': {'type': 'str'},
        'proxyBackupHost': {'type': 'str'},
        'serverNetworkInterface': {'type': 'str'},
        'priority': {'type': 'str'},
        'resourceId': {'type': 'str'},
        'physicalClientParallelism': {'type': 'bool'},
        'saveSessionDistribution': {'type': 'str'},
        'indexPath': {'type': 'str'},
        'executablePath': {'type': 'str'},
        'backupTargetDisks': {'type': 'str'},
        'ownerNotification': {'type': 'str'},
        'centralizedLogCollection': {'type': 'str'},
        'recoverStorageNodes': {'type': 'list'},
        'archiveServices': {'type': 'bool'},
        'allSaveSetExpired': {'type': 'bool'},
        'nasManagementUser': {'type': 'str'},
        'nasManagementPassword': {'type': 'str', 'no_log': False},
        'nasManagementName': {'type': 'str'},
        'nasFileAccessUser': {'type': 'str'},
        'nasFileAccessPassword': {'type': 'str'},
        'indexBackupContent': {'type': 'bool'},
        'field_params': {'type': 'list'},
        'query_params': {'type': 'dict'},
        'tags': {'type': 'list'},
        'comment': {'type': 'str'},
        'name': {'type': 'str'},
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
    url = f'https://{server}:{port}/nwrestapi/v3/global'
    failed, changed, msg, resp_msg = False, False, "", dict()
    resp_msg['responses'] = []
    resp_msg['msg'] = []
    api_initialize = ClientsApi(auth=auth, url=url)

    if state == 'get':
        if module.params['name'] is not None:
            if len(module.params['name']) > 0:
                client_name = module.params['name']
                response = api_initialize.get_client(client_id=client_name, field_params=module.params['field_params'])
                resp_msg['responses'].append(response)
        else:
            response = api_initialize.get_clients(field_params=module.params['field_params'],
                                                  query_params=module.params['query_params'])
            resp_msg['responses'].append(response)
    elif state == 'create':
        client_name = module.params['name']
        body = params
        del body['state']
        response = api_initialize.post_client(body=body)
        resp_msg['responses'].append(response)
        msg = 'Client %s Created Successfully' % client_name
        resp_msg['msg'].append(msg)
    elif state == 'modify':
        resource_id = module.params['resourceId']
        body = params
        del body['state']
        del body['resourceId']
        if 'backup_id' in params:
            backup_id = params['backup_id']
            response = api_initialize.put_client_backup(body=body, client_id=resource_id, backup_id=backup_id)
        else:
            response = api_initialize.put_client(body=body, client_id=resource_id)
        resp_msg['responses'].append(response)
        msg = response.text
        resp_msg['msg'].append(msg)

    elif state == 'delete':
        client_name = module.params['name']
        response = api_initialize.delete_client(client_id=client_name)
        resp_msg['responses'].append(response)
        msg = 'Client %s deleted Successfully' % client_name
        resp_msg['msg'].append(msg)

    elif state == 'run_backup':
        client_name = module.params['name']
        body = params
        del body['state']
        response = api_initialize.client_op_backup(body=body, client_id=client_name)
        resp_msg['responses'].append(response)
        msg = response.text
        resp_msg['msg'].append(msg)

    elif state == 'get_agents':
        client_name = module.params['name']
        if 'agent_type' in params:
            func = 'get_client_%s' % params['agent_type']
            response = eval('api_initialize.%s(client_id=client_name)' % func)
            resp_msg['responses'].append(response)
            resp_msg['msg'].append(response.text)
        else:
            response = api_initialize.get_client_agents(client_id=client_name)
            resp_msg['responses'].append(response)
            resp_msg['msg'].append(response.text)
    elif state == 'get_instances':
        client_name = module.params['name']
        backup_id = params['backup_id']
        if 'instance_id' in params:
            instance_id = params['instance_id']
            response = api_initialize.get_client_backup_instance(client_id=client_name, backup_id=backup_id,
                                                                 instance_id=instance_id)
            resp_msg['responses'].append(response)
            resp_msg['msg'].append(response.text)
        else:
            response = api_initialize.get_client_backup_instances(client_id=client_name, backup_id=backup_id)
            resp_msg['responses'].append(response)
            resp_msg['msg'].append(response.text)

    elif state == 'get_indexes':
        client_name = module.params['name']
        response = api_initialize.get_client_indexes(client_id=client_name)
        resp_msg['responses'].append(response)
        resp_msg['msg'].append(response.text)
    elif state == 'get_backups':
        client_name = module.params['name']
        if 'backup_id' in params:
            backup_id = params['backup_id']
            response = api_initialize.get_client_backup(client_id=client_name, backup_id=backup_id)
            resp_msg['responses'].append(response)
            resp_msg['msg'].append(response.text)
        else:
            response = api_initialize.get_client_backups(client_id=client_name)
            resp_msg['responses'].append(response)
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



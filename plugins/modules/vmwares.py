#!/usr/bin/python3
# Copyright ©️ 2022 Dell Inc. or its subsidiaries.
from __future__ import (absolute_import, division, print_function)
import urllib3
urllib3.disable_warnings()
import json
from ansible.module_utils.basic import AnsibleModule
from ..module_utils.vmware_api import vmwareApi

__metaclass__ = type

DOCUMENTATION = r'''
module: vmware
short_description: ''
description: ''
version_added: ''
options:
  state:
    type: str
    choices:
    - create, delete, update, get, inspect, start
    required: true
    description: 'Choose state as per the action you want to perform'
  operation:
    type: str
    choices:
    - protected-vms, vcenters, refresh-vcenters, vcenters-plugin, protected-vm-backups,
      protected-vm-backups-instances, protected-vm-backups-instances, recover-backups-instances,
      mount-backups-instances, vm-recover, mount-backups, vcenter-vms, vm-backup,
      active-vms, vproxies, register-vproxies, redeployment
    description: 'Choose operation you want to perform'
  cloudDeployment:
    type: bool
    description: 'This attribute indicates whether the hypervisor is running on the cloud.'
  hostname:
    type: str
    description: 'This attribute specifies the hostname of the server hosting the virtual machine monitor.'
  userName:
    type: str
    description: 'This attribute specifies the username of the virtual machine monitor.'
  userPassword:
    type: str
    no_log: false
    description: 'This attribute specifies the password of the virtual machine monitor.'
  snapshotFreeSpaceWarningThreshold:
    type: str
    description: 'This attribute specifies an integer value in the range of 0 - 100, indicating the percentage Freespace value above or equal to which a warning will be issued of low datastore storage availability for the current backup request.'
  snapshotFreeSpaceFailureThreshold:
    type: str
    description: 'This attribute specifies an integer in the range of 0 - 100, indicating the percentage Freespace value above or equal to which the backup request will be failed citing lack of datastore Freespace available to take a snapshot.'
  httpPort:
    type: str
    description: 'This attribute specifies the vCenter http port number, the default value is 80.'
  httpsPort:
    type: str
    description: 'This attribute specifies the vCenter https port number, the default value is 443.'
  vm-uuid:
    type: str
    description: 'This attribute specifies the Universal Unique Identifier of the VM.'
  backupId:
    type: str
    description: 'is the value of the id attribute in the backup resource.'
  retentionTime:
    type: str
    description: "This attribute specifies the save set expiry time. It determines how long the NetWorker server maintains save set entries in the media database and client file indexes in yyyy-MM-dd'T'HH:mm:ssXXX (2020-07-18T22:29:47+05:30) format. Ensure that the retention time is always greater or equal to browse time. The forever retention time value is defined as Fri Dec 31 9999 23:59:59. To keep the retention time value to indefinite/forever, provide the value of this attribute to Fri Dec 31 9999 or later in specified format."
  browseTime:
    type: str
    description: "This attribute specifies the save set browse time. It determines the time period for which the save sets remain browsable in the format yyyy-MM-dd'T'HH:mm:ssXXX (2020-07-18T22:29:47+05:30). Ensure that browse time is always lower or equal to retention time. The forever browse time value is defined as Fri Dec 31 9999 23:59:59. To keep the browse time value to indefinite/forever, provide the value of this attribute to Fri Dec 31 9999 or later in specified format."
  instanceId:
    type: str
    description: 'This attribute specifies the backup instance identifier.'
  recoverMode:
    type: str
    choices:
    - Revert, Instant, New, Disk, Application, FLR, Emergency
    description: 'This is a mandatory attribute. This attribute specifies the type of the restore.'
  vCenterHostname:
    type: str
    description: 'This is a mandatory attribute when recoverMode is set to "New", "Instant", "Disk", or "Emergency"; otherwise, it is not supported. This attribute specifies to which vCenter or ESX the VM or disk is restored.'
  mountJobId:
    type: str
    description: 'This is a mandatory attribute when recoverMode is set to "Application"; otherwise, it is not supported. This attribute specifies the mount job ID to be used by the restore session.'
  vmwareVmFlrOptions:
    type: dict
    description: 'This is a mandatory attribute when recoverMode is set to "FLR"; otherwise, it is not supported. This atribute specifies the target guest VM where the application recovery will be performed.'
    suboptions:
      terminateMountSession:
        type: bool
        description: 'This attribute specifies whether the mount session should be terminated at the end of recovery.'
      overwrite:
        type: bool
        description: 'This attribute specifies whether the files should be forcefully overwritten if they are present in the destination directory'
      itemsToRecover:
        type: list
        description: 'This attribute specifies the list of items to be recovered.'
      recoveryDestination:
        type: str
        description: 'This attribute specifies the destination on the target VM to which the recovered files will be copied.'
      elevateUser:
        type: str
        description: 'This attribute specifies whether the recover has to be performed with elevated (administrator) authority.'
  installFlrAgent:
    type: bool
    description: 'Install FLR Agent. Use when performing file level recovery'
  targetVCenterHostname:
    type: str
    description: 'Target vCenter hostname. Use when performing file level recovery'
  targetVmAdminUserId:
    type: str
    description: 'Target VM admin user ID Use when performing file level recovery'
  targetVmAdminUserPassword:
    type: str
    description: 'Target VM admin user password. Use when performing file level recovery. Use ansible Vault recommended.'
  targetVmName:
    type: str
    description: 'Target VM name. Use when performing file level recovery'
  targetVmUserId:
    type: str
    description: 'Target VM user id. Use when performing file level recovery'
  targetVmUserPassword:
    type: str
    description: 'Target VM user password. Use when performing file level recovery'
  uninstallFlrAgent:
    type: bool
    description: 'Uninstall FLR agent after restore'
  vProxy:
    type: str
    description: 'Virtual Proxy hostname'
  backupDeviceExportPath:
    type: str
    description: 'This attribute specifies the export path for the device.'
  targetVmMoref:
    type: str
    description: 'This attribute specifies the target VM moref.'
  vproxy-mount-session-id:
    type: str
    description: 'Value of the vProxyMountSessionId attribute in the vproxy mount job resource.'
  currentWorkingDirectory:
    type: str
    description: 'Current working directory during FLR restore'
  vproxy-browse-session-id:
    type: str
    description: 'Value of the vProxBrowseSessionId attribute in the vproxy mount job resource.'
  applicationData:
    type: str
    description: 'Application data'
  applicationName:
    type: str
    description: 'Application Name'
  applicationRestoreSavesets:
    type: dict
    description: 'Application Restore savesets'
    suboptions:
      applicationData:
        type: str
        description: 'Application Data'
      backupId:
        type: str
        description: 'Backup ID'
      instanceId:
        type: str
        description: 'Instance ID'
  clusterComputeResourceMoref:
    type: str
    description: 'This is an optional attribute when recoverMode is set to "New" or "Instant"; otherwise, it is not supported. Either clusterComputeResourceMoref or computeResourceMoref needs to be set to specify under which host or cluster the VM will be restored.'
  computeResourceMoref:
    type: str
    description: 'This is an optional attribute when recoverMode is set to "New" or "Instant"; otherwise, it is not supported. Either clusterComputeResourceMoref or computeResourceMoref needs to be set to specify under which host or cluster the VM will be restored.'
  datacenterMoref:
    type: str
    description: 'This is a mandatory attribute when recoverMode is set to "New" or "Instant"; otherwise, it is not supported. This attribute specifies to which data center the VM is restored.'
  datastoreMoref:
    type: str
    description: 'This is a mandatory attribute when recoverMode is set to "New" or "Emergency"; otherwise, it is not supported. This attribute specifies to which datastore VM files are restored.'
  debugLevel:
    type: str
    description: 'This attribute specifies the debug level to be used during restore.'
  deleteExistingBackingFile:
    type: bool
    description: 'This is a mandatory attribute when recoverMode is set to "Revert" and when the configuration recovery is also set; otherwise, it is not supported. This attribute specifies whether the existing disk will be deleted in case of disk configuration mismatch'
  disks:
    type: dict
    description: 'Disk related paramerters'
    suboptions:
      datastoreMoref:
        type: str
        description: 'This attribute specifies the Managed Object Reference ID associated with the destination datastore for this disk. This is a mandatory attribute.'
      key:
        type: str
        description: 'This attribute specifies the key of the disk, which can be retrieved from the vmInformation property of a backup. This is a mandatory attribute.'
      name:
        type: str
        description: 'This attribute specifies the name of the disk, which can be retrieved from the vmInformation property of a backup. This is a mandatory attribute.'
  hostMoref:
    type: str
    description: 'This is an optional attribute when recoverMode is set to "New" or "Instant"; otherwise, it is not supported. This attribute specifies to which host the VM is restored. This is not required when restoring to a DRS-enabled cluster.'
  jobName:
    type: str
    description: 'This is an optional attribute for all recoverMode values. This attribute specifies the name of the job that will be created.'
  powerOn:
    type: bool
    description: 'This is a mandatory attribute when recoverMode is set to "Revert", "Instant", "New", "Disk", or "Emergency"; otherwise, it is not supported. This attribute specifies whether to power on the VM at the end of the restore.'
  reconnectNic:
    type: bool
    description: 'This is a mandatory attribute when recoverMode is set to "Revert", "Instant", "New", "Disk", or "Emergency"; otherwise, it is not supported. This attribute specifies whether to reconnect the NIC of the VM at the end of the restore'
  resourcePoolMoref:
    type: str
    description: 'This is an optional attribute when recoverMode is set to "New" or "Instant"; otherwise, it is not supported. This attribute specifies the resource pool to which the VM will be restored.'
  revertConfiguration:
    type: bool
    description: 'This is a mandatory attribute when recoverMode is set to "Revert"; otherwise, it is not supported. This attribute specifies whether to revert the VM configuration.'
  stagingPool:
    type: str
    description: 'This is an optional attribute for all recoverMode values. This attribute specifies which staging pool to use on the DD device when restoring from a clone.'
  vmEmergencyRecoverCleanupOptions:
    type: dict
    description: 'This is a mandatory attribute when recoverMode is set to "Emergency"; otherwise, it is not supported. This attribute specifies the options for cleaning up ESX, proxy, and client resources at the end of the emergency recovery.'
    suboptions:
      deleteEsxClient:
        type: bool
        description: 'This attribute specifies whether the ESX client must be deleted at the end of emergency recovery.'
      deleteEsxHypervisor:
        type: bool
        description: 'This attribute specifies whether the ESX hypervisor resource must be deleted at the end of emergency recovery.'
      deleteVproxy:
        type: bool
        description: 'This attribute specifies whether the vProxy resource must be deleted at the end of emergency recovery.'
      vCenterHostnameForVproxy:
        type: str
        description: 'This attribute specifies to which vCenter the vProxy must be associated at the end of emergency recovery. Used only if the deleteVproxy option is unset or set to "false".'
  vmFolderMoref:
    type: str
    description: 'This is a mandatory attribute when recoverMode is set to "New"; otherwise, it is not supported. This attribute specifies the VM folder under which the VM will be recovered.'
  vmGuestLogin:
    type: dict
    description: 'This is a mandatory attribute when recoverMode is set to "Application"; otherwise, it is not supported. This attribute specifies the target guest VM where the application recovery will be performed.'
    suboptions:
      installAppAgent:
        type: bool
        description: 'This attribute specifies whether to install the Microsoft Virtual Machine Application Agent (MSVMAPPAGENT) which is required for application-consistent VMware recover.'
      targetVmAdminUserId:
        type: str
        description: 'This attribute specifies the target VM administrator user ID.'
      targetVmAdminUserPassword:
        type: str
        no_log: false
        description: 'This attribute specifies the target VM administrator user password.'
      targetVmUserId:
        type: str
        description: 'This attribute specifies the target VM user ID.'
      targetVmUserPassword:
        type: str
        no_log: false
        description: 'This attribute specifies the target VM user password.'
      uninstallAppAgent:
        type: bool
        description: 'This attribute specifies whether to uninstall the Microsoft Virtual Machine Application Agent (MSVMAPPAGENT) which is required for application-consistent VMware recover.'
  vmMoref:
    type: str
    description: 'This is a mandatory attribute when recoverMode is set to "Disk" or "Application"; otherwise, it is not supported. This attribute specifies to which VM the restored disk will be attached.'
  vmName:
    type: str
    description: 'This is a mandatory attribute when recoverMode is set to "New", "Instant", "Disk", "Application", or "Emergency"; otherwise, it is not supported. This attribute specifies either the restored VM name or, when recoverMode is "Disk" or "Application", the existing VM name to which the restored disk will be attached.'
  vProxyHostname:
    type: str
    description: 'This is a mandatory attribute when recoverMode is set to "Emergency". It is optional when recoverMode is set to "Revert", "New", "Instant", "Disk", or "Application"; otherwise, it is not supported. This attribute specifies the vProxy to be used for recovery.'
  policy:
    type: str
    description: 'This attribute specifies the policy name of the backup.'
  workflow:
    type: str
    description: 'This attribute specifies the workflow name of the backup.'
  isAdhoc:
    type: bool
    description: 'This attribute specifies whether the backup needs to be run in adhoc mode.'
  idleTimeout:
    type: str
    description: 'This attribute specifies the idle timeout in seconds for the browse session.'
  cacheRetentionSeconds:
    type: str
    description: 'This attribute specifies the time in seconds after which cached contents of the current working directory will be considered stale.'
  browseDestination:
    type: bool
    description: 'This attribute specifies whether the destination VM should be browsed. The default value is false.'
  osType:
    type: str
    choices:
    - Windows, Linux
    description: 'This attribute specifies the destination VM operating system type.'
  elevateUser:
    type: bool
    description: 'This attribute specifies whether the browse has to be performed with elevated (administrator) authority.'
  enabled:
    type: str
    description: 'This attribute indicates whether the VM proxy is available for use.'
  maxHotaddSessions:
    type: str
    description: 'This attribute specifies the maximum VM clients this vProxy appliance will concurrently support through HotAdd.'
  maxNbdSessions:
    type: str
    description: 'This attribute specifies the maximum VM sessions this vProxy appliance will concurrently support through NBD.'
  vProxyPort:
    type: str
    description: 'This attribute specifies the TCP port number of the proxy service.'
  datastores:
    type: list
    description: 'This attribute specifies the datastores which this proxy can access.'
  encryptNbdSessions:
    type: str
    description: 'This attribute indicates whether to enable NBDSSL, which encrypts NBD sessions with SSL. This option takes effect only if the maximum NBD sessions attribute is set to a positive value.'
  forceRegister:
    type: str
    description: 'This attribute specifies whether or not to force register.'
  maxHotaddDisks:
    type: str
    description: 'This attribute specifies the maximum number of virtual disks that NetWorker can concurrently hotadd to the vProxy appliance.'
  fallbackToNBDForIDEDisk:
    type: bool
    description: 'This attribute specifies whether fallback to NBD session is enabled or disabled when IDE disks are present.'
  comment:
    type: str
    description: 'This attribute specifies any user-defined description of this resource or other explanatory remarks.'
  comments:
    type: str
    description: 'This attribute specifies an informational comment.'
  timeoutInMins:
    type: str
    description: 'This attribute specifies timeout in minutes.'
  rootPasswd:
    type: str
    description: 'This attribute is required if the deployed vProxy has a different root password.'
  adminPasswordAsRoot:
    type: bool
    description: 'This attribute value is true if the deployed vProxy has the same admin and root passwords.'
  query_params:
    type: dict
    description: 'query parameters'
  field_params:
    type: list
    description: 'field parameters'
'''

EXAMPLES = r'''
    - name: Get all vCenter names registered in NetWorker Server
        dellemc.networker.vmwares:
        state: get
        operation: vcenters 
        register: vcenters

    - name: Get information about perticular vCenter
      dellemc.networker.vmwares:
        state: get
        operation: vcenters
        vCenterHostname: x001usx14vcs001.usx1lab.xstream360.cloud
    
    - name: Get all vProxy names
      dellemc.networker.vmwares:
        state: get
        operation: vproxy 
'''


def check_fields(fields, params):
    result = []
    for field in fields:
        if field in params:
            result.append(True)
        else:
            result.append(False)

    if all(result):
        return True
    else:
        return False


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
        'state': {'type': 'str', 'choices': ['create', 'delete', 'update', 'refresh', 'get', 'inspect', 'start', 'register', 'redeploy'],
                  'required': True},
        'operation': {'type': 'str', 'choices': ['protected-vms', 'vcenters', 'vcenters-plugin',
                                                 'protected-vm-backups', 'protected-vm-backups-instances',
                                                 'recover-backups-instances',
                                                 'mount-backups-instances', 'vm-recover', 'mount-backups',
                                                 'vcenter-vms', 'vm-backup', 'active-vms', 'vproxy',
                                                 'redeployment', 'vmbrowse-session']},
        'cloudDeployment': {'type': 'bool'},
        'hostname': {'type': 'str'},
        'userName': {'type': 'str'},
        'userPassword': {'type': 'str', 'no_log': False},
        'snapshotFreeSpaceWarningThreshold': {'type': 'str'},
        'snapshotFreeSpaceFailureThreshold': {'type': 'str'},
        'httpPort': {'type': 'str'},
        'httpsPort': {'type': 'str'},
        'vm-uuid': {'type': 'str'},
        'backupId': {'type': 'str'},
        'retentionTime': {'type': 'str'},
        'browseTime': {'type': 'str'},
        'instanceId': {'type': 'str'},
        'recoverMode': {'type': 'str', 'choices': ['Revert', 'Instant', 'New', 'Disk', 'Application', 'FLR', 'Emergency']},
        'vCenterHostname': {'type': 'str'},
        'mountJobId': {'type': 'str'},
        'vmwareVmFlrOptions': {'type': 'dict', 'options': {
            'terminateMountSession': {'type': 'bool'},
            'overwrite': {'type': 'bool'},
            'itemsToRecover': {'type': 'list'},
            'recoveryDestination': {'type': 'str'},
            'elevateUser': {'type': 'str'},
        }},
        'installFlrAgent': {'type': 'bool'},
        'targetVCenterHostname': {'type': 'str'},
        'targetVmAdminUserId': {'type': 'str'},
        'targetVmAdminUserPassword': {'type': 'str'},
        'targetVmName': {'type': 'str'},
        'targetVmUserId': {'type': 'str'},
        'targetVmUserPassword': {'type': 'str'},
        'uninstallFlrAgent': {'type': 'bool'},
        'vProxy': {'type': 'str'},
        'backupDeviceExportPath': {'type': 'str'},
        'targetVmMoref': {'type': 'str'},
        'vproxy-mount-session-id': {'type': 'str'},
        'currentWorkingDirectory': {'type': 'str'},
        'vproxy-browse-session-id': {'type': 'str'},
        'applicationData': {'type': 'str'},
        'applicationName': {'type': 'str'},
        'applicationRestoreSavesets': {'type': 'dict', 'options':{
            'applicationData': {'type': 'str'},
            'backupId': {'type': 'str'},
            'instanceId': {'type': 'str'},
        }},
        'clusterComputeResourceMoref': {'type': 'str'},
        'computeResourceMoref': {'type': 'str'},
        'datacenterMoref': {'type': 'str'},
        'datastoreMoref': {'type': 'str'},
        'debugLevel': {'type': 'str'},
        'deleteExistingBackingFile': {'type': 'bool'},
        'disks': {'type': 'dict', 'options': {
            'datastoreMoref': {'type': 'str'},
            'key': {'type': 'str'},
            'name': {'type': 'str'},
        }},
        'hostMoref': {'type': 'str'},
        'jobName': {'type': 'str'},
        'powerOn': {'type': 'bool'},
        'reconnectNic': {'type': 'bool'},
        'resourcePoolMoref': {'type': 'str'},
        'revertConfiguration': {'type': 'bool'},
        'stagingPool': {'type': 'str'},
        'vmEmergencyRecoverCleanupOptions': {'type': 'dict', 'options': {
            'deleteEsxClient': {'type': 'bool'},
            'deleteEsxHypervisor': {'type': 'bool'},
            'deleteVproxy': {'type': 'bool'},
            'vCenterHostnameForVproxy': {'type': 'str'}
        }},
        'vmFolderMoref': {'type': 'str'},
        'vmGuestLogin': {'type': 'dict', 'options': {
            'installAppAgent': {'type': 'bool'},
            'targetVmAdminUserId': {'type': 'str'},
            'targetVmAdminUserPassword': {'type': 'str', 'no_log': False},
            'targetVmUserId': {'type': 'str'},
            'targetVmUserPassword': {'type': 'str', 'no_log': False},
            'uninstallAppAgent': {'type': 'bool'}
        }},
        'vmMoref': {'type': 'str'},
        'vmName': {'type': 'str'},
        'vProxyHostname': {'type': 'str'},
        'policy': {'type': 'str'},
        'workflow': {'type': 'str'},
        'isAdhoc': {'type': 'bool'},
        'idleTimeout': {'type': 'str'},
        'cacheRetentionSeconds': {'type': 'str'},
        'browseDestination': {'type': 'bool'},
        'osType': {'type': 'str', 'choices': ['Windows', 'Linux']},
        'elevateUser': {'type': 'bool'},
        'enabled': {'type': 'str'},
        'maxHotaddSessions': {'type': 'str'},
        'maxNbdSessions': {'type': 'str'},
        'vProxyPort': {'type': 'str'},
        'datastores': {'type': 'list'},
        'encryptNbdSessions': {'type': 'str'},
        'forceRegister': {'type': 'str'},
        'maxHotaddDisks': {'type': 'str'},
        'fallbackToNBDForIDEDisk': {'type': 'bool'},
        'comment': {'type': 'str'},
        'comments': {'type': 'str'},
        'timeoutInMins': {'type': 'str'},
        'rootPasswd': {'type': 'str'},
        'adminPasswordAsRoot': {'type': 'bool'},
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
    api_initialize = vmwareApi(auth=auth, url=url)

    if state == 'get':
        if module.params['operation'] == 'vcenters':
            if 'hostname' in params:
                response = api_initialize.get_v_center(vcenter_hostname=module.params['hostname'])
                resp_msg['responses'].append(response)
            else:
                response = api_initialize.get_v_centers()
                resp_msg['responses'].append(response)
        elif module.params['operation'] == 'protected-vms':
            if 'hostname' in params and 'vm-uuid' in params:
                response = api_initialize.get_v_center_protected_vm(vcenter_hostname=module.params['hostname'], vm_uuid=module.params['vm-uuid'])
                resp_msg['responses'].append(response)
            elif 'hostname' in params and 'vm-uuid' not in params:
                response = api_initialize.get_v_center_protected_vms(vcenter_hostname=module.params['hostname'])
                resp_msg['responses'].append(response)
            else:
                response = api_initialize.get_v_mware_protected_vms()
                resp_msg['responses'].append(response)
        elif module.params['operation'] == 'protected-vm-backups':
            if 'hostname' in params and 'vm-uuid' in params:
                response = api_initialize.get_v_center_protected_vm_backups(vcenter_hostname=module.params['hostname'],
                                                                            vm_uuid=module.params['vm-uuid'])
                resp_msg['responses'].append(response)
        elif module.params['operation'] == 'protected-vm-backups-instances':
            fields_to_check = ['hostname', 'vm-uuid', 'backupId']
            check_status = check_fields(fields_to_check, params)
            if check_status:
                response = api_initialize.get_v_center_protected_vm_backup_instances(vcenter_hostname=module.params['hostname'],
                                                                                     vm_uuid=module.params['vm-uuid'],
                                                                                     backup_id=module.params['backupId'])
                resp_msg['responses'].append(response)
        elif module.params['operation'] == 'mount-backups-instances':
            fields_to_check = ['hostname', 'vm-uuid', 'backupId', 'instanceId', 'vproxy-mount-session-id']
            check_status = check_fields(fields_to_check, params)
            if check_status:
                response = api_initialize.get_instance_v_proxy_vm_mount_session_response(vcenter_hostname=module.params['hostname'],
                                                                                     vm_uuid=module.params['vm-uuid'],
                                                                                     backup_id=module.params['backupId'],
                                                                                         instance_id=module.params['instanceId'],
                                                                                         vproxy_mount_session_id=module.params['vproxy-mount-session-id'])
                resp_msg['responses'].append(response)
        elif module.params['operation'] == 'vmbrowse-session':
            fields_to_check1 = ['hostname', 'vm-uuid', 'backupId', 'instanceId', 'vproxy-mount-session-id', 'vproxy-browse-session-id']
            check_status1 = check_fields(fields_to_check1, params)
            fields_to_check2 = ['hostname', 'vm-uuid', 'backupId', 'instanceId', 'vproxy-mount-session-id']
            check_status2 = check_fields(fields_to_check2, params)
            fields_to_check3 = ['hostname', 'vm-uuid', 'backupId', 'vproxy-mount-session-id', 'vproxy-browse-session-id']
            check_status3 = check_fields(fields_to_check3, params)
            fields_to_check4 = ['hostname', 'vm-uuid', 'backupId', 'vproxy-browse-session-id']
            check_status4 = check_fields(fields_to_check4, params)
            if check_status1:
                response = api_initialize.get_instance_v_proxy_vm_browse_session_response(vcenter_hostname=module.params['hostname'],
                                                                                     vm_uuid=module.params['vm-uuid'],
                                                                                     backup_id=module.params['backupId'],
                                                                                         instance_id=module.params['instanceId'],
                                                                                         vproxy_mount_session_id=module.params['vproxy-mount-session-id'],
                                                                                          vproxy_browse_session_id=module.params['vproxy-browse-session-id'])
                resp_msg['responses'].append(response)

            elif check_status2:
                response = api_initialize.get_instance_v_proxy_vm_browse_session_response_list(vcenter_hostname=module.params['hostname'],
                                                                                     vm_uuid=module.params['vm-uuid'],
                                                                                     backup_id=module.params['backupId'],
                                                                                         instance_id=module.params['instanceId'],
                                                                                         vproxy_mount_session_id=module.params['vproxy-mount-session-id'])
                resp_msg['responses'].append(response)
            elif check_status3:
                response = api_initialize.get_backup_v_proxy_vm_browse_session_response(vcenter_hostname=module.params['hostname'],
                                                                                     vm_uuid=module.params['vm-uuid'],
                                                                                     backup_id=module.params['backupId'],
                                                                                         vproxy_mount_session_id=module.params['vproxy-mount-session-id'],
                                                                                        vproxy_browse_session_id=module.params['vproxy-browse-session-id'])
                resp_msg['responses'].append(response)
            elif check_status4:
                response = api_initialize.get_backup_v_proxy_vm_browse_session_response_list(vcenter_hostname=module.params['hostname'],
                                                                                     vm_uuid=module.params['vm-uuid'],
                                                                                     backup_id=module.params['backupId'],
                                                                                         vproxy_mount_session_id=module.params['vproxy-mount-session-id'])
                resp_msg['responses'].append(response)
        elif module.params['operation'] == 'vmbrowse-session-contents':
            fields_to_check1 = ['hostname', 'vm-uuid', 'backupId', 'instanceId', 'vproxy-mount-session-id', 'vproxy-browse-session-id']
            check_status1 = check_fields(fields_to_check1, params)
            fields_to_check2 = ['hostname', 'vm-uuid', 'backupId', 'vproxy-mount-session-id', 'vproxy-browse-session-id']
            check_status2 = check_fields(fields_to_check2, params)
            if check_status1:
                response = api_initialize.get_instance_v_proxy_vm_browse_session_contents(vcenter_hostname=module.params['hostname'],
                                                                                     vm_uuid=module.params['vm-uuid'],
                                                                                     backup_id=module.params['backupId'],
                                                                                         instance_id=module.params['instanceId'],
                                                                                         vproxy_mount_session_id=module.params['vproxy-mount-session-id'],
                                                                                          vproxy_browse_session_id=module.params['vproxy-browse-session-id'])
                resp_msg['responses'].append(response)
            elif check_status2:
                response = api_initialize.get_backup_v_proxy_vm_browse_session_contents(vcenter_hostname=module.params['hostname'],
                                                                                     vm_uuid=module.params['vm-uuid'],
                                                                                     backup_id=module.params['backupId'],
                                                                                         vproxy_mount_session_id=module.params['vproxy-mount-session-id'],
                                                                                          vproxy_browse_session_id=module.params['vproxy-browse-session-id'])
                resp_msg['responses'].append(response)
        elif module.params['operation'] == 'mount-backups':
            fields_to_check = ['hostname', 'vm-uuid', 'backupId', 'vproxy-mount-session-id']
            check_status = check_fields(fields_to_check, params)
            if check_status:
                response = api_initialize.get_backup_v_proxy_vm_mount_session_response(vcenter_hostname=module.params['hostname'],
                                                                                     vm_uuid=module.params['vm-uuid'],
                                                                                     backup_id=module.params['backupId'],
                                                                                         vproxy_mount_session_id=module.params['vproxy-mount-session-id'],
                                                                                         )
                resp_msg['responses'].append(response)
        elif module.params['operation'] == 'vcenter-vms':
            if 'hostname' in params and 'vm-uuid' in params:
                response = api_initialize.get_v_center_vm(vcenter_hostname=module.params['hostname'], vm_uuid=module.params['vm-uuid'])
                resp_msg['responses'].append(response)
            elif 'hostname' in params and 'vm-uuid' not in params:
                response = api_initialize.get_v_center_vms(vcenter_hostname=module.params['hostname'])
                resp_msg['responses'].append(response)
        elif module.params['operation'] == 'redeployment':
            if 'vProxyHostname' in params:
                response = api_initialize.get_v_proxy_redeploy(id=module.params['vProxyHostname'])
                resp_msg['responses'].append(response)
        elif module.params['operation'] == 'vm-backup':
            if 'hostname' in params and 'vm-uuid' in params:
                response = api_initialize.get_v_mware_v_center_vm_protection_details(vcenter_hostname=module.params['hostname'], vm_uuid=module.params['vm-uuid'])
                resp_msg['responses'].append(response)
        elif module.params['operation'] == 'active-vms':
            response = api_initialize.get_v_mware_vms()
            resp_msg['responses'].append(response)
        elif module.params['operation'] == 'vproxy':
            if 'vProxyHostname' in params:
                response = api_initialize.get_v_proxy(vproxy_hostname=module.params['vProxyHostname'])
                resp_msg['responses'].append(response)
            else:
                response = api_initialize.get_v_proxies()
                resp_msg['responses'].append(response)
    elif state == 'create':
        if module.params['operation'] == 'vmbrowse-session':
            fields_to_check1 = ['hostname', 'vm-uuid', 'backupId', 'vproxy-mount-session-id', 'instanceId']
            check_status1 = check_fields(fields_to_check1, params)
            fields_to_check2 = ['hostname', 'vm-uuid', 'backupId', 'vproxy-mount-session-id']
            check_status2 = check_fields(fields_to_check2, params)
            if check_status1:
                body = params
                del body['state']
                for item in fields_to_check1:
                    del body[item]
                response = api_initialize.post_instance_v_proxy_vm_browse_session_request(vcenter_hostname=module.params['hostname'],
                                                                                        vm_uuid=module.params['vm-uuid'],
                                                                                        backup_id=module.params['backupId'],
                                                                             vproxy_mount_session_id=module.params['vproxy-mount-session-id'], instance_id=module.params['instanceId'], body=body)
                resp_msg['responses'].append(response)
                msg = 'Created VM Browse session successfully.'
                resp_msg['msg'].append(msg)
            elif check_status2:
                body = params
                del body['state']
                for item in fields_to_check1:
                    del body[item]
                response = api_initialize.post_backup_v_proxy_vm_browse_session_request(
                    vcenter_hostname=module.params['hostname'],
                    vm_uuid=module.params['vm-uuid'],
                    backup_id=module.params['backupId'],
                    vproxy_mount_session_id=module.params['vproxy-mount-session-id'], body=body)
                resp_msg['responses'].append(response)
        elif module.params['operation'] == 'vcenters':
            body = params
            del body['state']

            response = api_initialize.post_v_center(body=body)
            resp_msg['responses'].append(response)
            msg = 'vcenter %s added successfully in NetWorker server' % params['hostname']
            resp_msg['msg'].append(msg)
        elif module.params['operation'] == 'recover-backups-instances':
            fields_to_check = ['hostname', 'vm-uuid', 'backupId', 'instanceId']
            check_status = check_fields(fields_to_check, params)
            if check_status:
                body = params
                del body['state']
                for item in fields_to_check:
                    del body[item]
                response = api_initialize.post_v_center_protected_vm_backup_instance_recover(
                    vcenter_hostname=module.params['hostname'],
                    vm_uuid=module.params['vm-uuid'],
                    backup_id=module.params['backupId'],
                    body=body)
                resp_msg['responses'].append(response)
                msg = 'Successfully Started restore for VM %s' % module.params['vm-uuid']
                resp_msg['msg'].append(msg)
        elif module.params['operation'] == 'mount-backups-instances':
            fields_to_check = ['hostname', 'vm-uuid', 'backupId', 'instanceId']
            check_status = check_fields(fields_to_check, params)
            if check_status:
                body = params
                del body['state']
                for item in fields_to_check:
                    del body[item]
                response = api_initialize.post_v_center_protected_vm_backup_instance_vm_mount(
                    vcenter_hostname=module.params['hostname'],
                    vm_uuid=module.params['vm-uuid'],
                    backup_id=module.params['backupId'],
                    body=body, instance_id=module.params['instanceId'])
                resp_msg['responses'].append(response)
                msg = 'Successfully mounted backup instance for VM %s' % module.params['vm-uuid']
                resp_msg['msg'].append(msg)
        elif module.params['operation'] == 'mount-backups':
            fields_to_check = ['hostname', 'vm-uuid', 'backupId']
            check_status = check_fields(fields_to_check, params)
            if check_status:
                body = params
                del body['state']
                for item in fields_to_check:
                    del body[item]
                response = api_initialize.post_v_center_protected_vm_backup_vm_mount(
                    vcenter_hostname=module.params['hostname'],
                    vm_uuid=module.params['vm-uuid'],
                    backup_id=module.params['backupId'],
                    body=body)
                resp_msg['responses'].append(response)
                msg = 'Successfully mounted backup for VM %s' % module.params['vm-uuid']
                resp_msg['msg'].append(msg)
        elif module.params['operation'] == 'vproxy':
            body = params
            del body['state']
            response = api_initialize.post_v_proxy(body=body)
            resp_msg['responses'].append(response)
            msg = 'Successfully created vproxy appliance resource %s on NetWorker Server' % module.params['vProxyHostname']
            resp_msg['msg'].append(msg)
    elif state == 'update':
        if module.params['operation'] == 'vcenters':
            if 'hostname' in params:
                body = params
                del body['state']
                del body['hostname']
                response = api_initialize.put_v_center(vcenter_hostname=module.params['hostname'], body=body)
                resp_msg['responses'].append(response)
                msg = 'Successfully updated vCenter %s on NetWorker Server' % module.params[
                    'hostname']
                resp_msg['msg'].append(msg)
        elif module.params['operation'] == 'protected-vm-backups':
            if 'hostname' in params and 'vm-uuid' in params and 'backupId' in params:
                body = params
                del body['state']
                del body['hostname']
                del body['backupId']
                del body['vm-uuid']
                response = api_initialize.put_vm_backup(vcenter_hostname=module.params['hostname'], body=body,
                                                        backup_id=module.params['backupId'], vm_uuid=module.params['vm-uuid'])
                resp_msg['responses'].append(response)
                msg = 'Successfully updated backup with backupId %s for VM %s' % (module.params['backupId'], module.params['vm-uuid'])
                resp_msg['msg'].append(msg)
        elif module.params['operation'] == 'vmbrowse-session':
            fields_to_check1 = ['hostname', 'vm-uuid', 'backupId', 'instanceId', 'vproxy-mount-session-id', 'vproxy-browse-session-id']
            check_status1 = check_fields(fields_to_check1, params)
            fields_to_check2 = ['hostname', 'vm-uuid', 'backupId', 'vproxy-mount-session-id', 'vproxy-browse-session-id']
            check_status2 = check_fields(fields_to_check2, params)
            if check_status1:
                body = params
                del body['state']
                for item in fields_to_check1:
                    del body[item]
                response = api_initialize.put_instance_v_proxy_vm_browse_session_request(vcenter_hostname=module.params['hostname'], body=body,
                                                        backup_id=module.params['backupId'], vm_uuid=module.params['vm-uuid'], instance_id=module.params['instanceId'],
                                                                                         vproxy_mount_session_id=module.params['vproxy-mount-session-id'],
                                                                                         vproxy_browse_session_id=module.params['vproxy-browse-session-id'])
                resp_msg['responses'].append(response)
                msg = 'Updated VM browse session.'
                resp_msg['msg'].append(msg)
            elif check_status2:
                body = params
                del body['state']
                for item in fields_to_check2:
                    del body[item]
                response = api_initialize.put_backup_v_proxy_vm_browse_session_request(vcenter_hostname=module.params['hostname'], body=body,
                                                        backup_id=module.params['backupId'], vm_uuid=module.params['vm-uuid'],
                                                                                         vproxy_mount_session_id=module.params['vproxy-mount-session-id'],
                                                                                         vproxy_browse_session_id=module.params['vproxy-browse-session-id'])
                resp_msg['responses'].append(response)
                msg = 'Updated VM browse session.'
                resp_msg['msg'].append(msg)
        elif module.params['operation'] == 'vproxy':
            if 'hostname' in params:
                body = params
                del body['state']
                del body['vProxyHostname']
                response = api_initialize.put_v_proxy(body=body, vproxy_hostname=module.params['vProxyHostname'])
                resp_msg['responses'].append(response)
                msg = 'Successfully updated vProxy %s' % params['vProxyHostname']
                resp_msg['msg'].append(msg)
    elif state == 'refresh':
        if module.params['operation'] == 'vcenters':
            if 'hostname' in params:
                response = api_initialize.post_v_center_op_refresh(vcenter_hostname=module.params['hostname'])
                resp_msg['responses'].append(response)
                msg = 'vCenter %s refreshed successfully' % module.params['hostname']
                resp_msg['msg'].append(msg)
            else:
                response = api_initialize.post_v_mware_op_refresh_v_centers()
                resp_msg['responses'].append(response)
                msg = 'All vcenters refreshed successfully'
                resp_msg['msg'].append(msg)
    elif state == 'install':
        if module.params['operation'] == 'vcenters-plugin':
            if 'hostname' in params:
                body = params
                del body['state']
                del body['hostname']
                response = api_initialize.post_v_center_plugin(vcenter_hostname=module.params['hostname'], body=body)
                resp_msg['responses'].append(response)
                msg = 'Initiated Install vcenter plugin on vcenter %s' % params['hostname']
    elif state == 'inspect':
        if module.params['operation'] == 'protected-vm-backups-instances':
            fields_to_check = ['hostname', 'vm-uuid', 'backupId', 'instanceId']
            check_status = check_fields(fields_to_check, params)
            if check_status:
                response = api_initialize.post_v_center_protected_vm_backup_instance_inspect_backup(vcenter_hostname=module.params['hostname'],
                                                                                                    vm_uuid=module.params['vm-uuid'],
                                                                                                    backup_id=module.params['backupId'],
                                                                                                    instance_id=module.params['instanceId'])
                resp_msg['responses'].append(response)
                msg = 'Initiated inspect task on backupId %s' % params['backupId']
                resp_msg['msg'].append(msg)
        elif module.params['operation'] == 'protected-vm-backups':
            fields_to_check = ['hostname', 'vm-uuid', 'backupId']
            check_status = check_fields(fields_to_check, params)
            if check_status:
                response = api_initialize.post_v_center_protected_vm_backup_inspect_backup(vcenter_hostname=module.params['hostname'],
                                                                                           vm_uuid=module.params['vm-uuid'],
                                                                                           backup_id=module.params['backupId'])
                resp_msg['responses'].append(response)
                msg = 'Initiated inspect task on backupId %s' % params['backupId']
                resp_msg['msg'].append(msg)
    elif state == 'start':
        if module.params['operation'] == 'vm-recover':
            fields_to_check = ['hostname', 'vm-uuid', 'backupId']
            check_status = check_fields(fields_to_check, params)
            if check_status:
                body = params
                del body['state']
                for item in fields_to_check:
                    del body[item]
                response = api_initialize.post_v_center_protected_vm_backup_recover(vcenter_hostname=module.params['hostname'],
                                                                                    vm_uuid=module.params['vm-uuid'],
                                                                                    backup_id=module.params['backupId'],
                                                                                    body=body)
                resp_msg['responses'].append(response)
                msg = 'Initiated recovery task on vm %s' % params['vm-uuid']
                resp_msg['msg'].append(msg)
        elif module.params['operation'] == 'vm-backup':
            fields_to_check = ['hostname', 'vm-uuid']
            check_status = check_fields(fields_to_check, params)
            if check_status:
                body = params
                del body['state']
                for item in fields_to_check:
                    del body[item]
                response = api_initialize.post_v_mware_v_center_vm_op_backup(vcenter_hostname=module.params['hostname'],
                                                                                    vm_uuid=module.params['vm-uuid'],
                                                                                    body=body)
                resp_msg['responses'].append(response)

    elif state == 'register':
        if module.params['operation'] == 'vproxy':
            body = params
            del body['state']
            response = api_initialize.post_op_register_v_proxy(body=body)
            resp_msg['responses'].append(response)

            msg = 'Initiated vproxy %s registration' % params['vProxyHostname']
            resp_msg['msg'].append(msg)
    elif state == 'redeploy':
        if module.params['operation'] == 'vproxy' and 'vProxyHostname' in params:
            body = params
            del body['state']
            response = api_initialize.post_v_proxy_redeploy(body=body, id=module.params['vProxyHostname'])
            resp_msg['responses'].append(response)
            msg = 'Initiated vproxy %s redeployment' % params['vProxyHostname']
            resp_msg['msg'].append(msg)
    elif state == 'delete':
        if module.params['operation'] == 'vcenters':
            if 'hostname' in params:
                response = api_initialize.delete_v_center(vcenter_hostname=module.params['hostname'])
                resp_msg['responses'].append(response)
                msg = 'Deleted vcenter %s registration on networker server' % params['hostname']
                resp_msg['msg'].append(msg)
        elif module.params['operation'] == 'vmbrowse-session':
            fields_to_check1 = ['hostname', 'vm-uuid', 'backupId', 'instanceId', 'vproxy-mount-session-id', 'vproxy-browse-session-id']
            check_status1 = check_fields(fields_to_check1, params)
            fields_to_check2 = ['hostname', 'vm-uuid', 'backupId', 'vproxy-mount-session-id', 'vproxy-browse-session-id']
            check_status2 = check_fields(fields_to_check2, params)
            if check_status1:
                response = api_initialize.delete_instance_v_proxy_vm_browse_session(vcenter_hostname=module.params['hostname'],
                                                                                            vm_uuid=module.params['vm-uuid'],
                                                                                            backup_id=module.params['backupId'],
                                                                                 vproxy_mount_session_id=module.params['vproxy-mount-session-id'],
                                                                                    instance_id=module.params['instanceId'])
                resp_msg['responses'].append(response)
                msg = 'Deleted vm browse session for instance %s' % params['instanceId']
                resp_msg['msg'].append(msg)
            elif check_status2:
                response = api_initialize.delete_backup_v_proxy_vm_browse_session(vcenter_hostname=module.params['hostname'],
                                                                                            vm_uuid=module.params['vm-uuid'],
                                                                                            backup_id=module.params['backupId'],
                                                                                 vproxy_mount_session_id=module.params['vproxy-mount-session-id'])
                resp_msg['responses'].append(response)
                msg = 'Deleted vm browse session for backup %s' % params['backupId']
                resp_msg['msg'].append(msg)
        elif module.params['operation'] == 'vproxy':
            if 'vProxyHostname' in params:
                response = api_initialize.delete_v_proxy(vproxy_hostname=module.params['vProxyHostname'])
                resp_msg['responses'].append(response)
                msg = 'Deleted vproxy %s' % params['vProxyHostname']
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



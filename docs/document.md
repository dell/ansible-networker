# Ansible Collection for Dell Technologies DataDomain
© 2022 Dell Inc. or its subsidiaries. All rights reserved. Dell and other trademarks are trademarks of Dell Inc. or its subsidiaries. Other trademarks may be trademarks of their respective owners.

## Contents
*   [alerts](#alerts)
*   [backups](#backups)
*   [clients](#clients)
*   [datadomains](#datadomains)
*   [devices](#devices)
*   [directives](#directives)
*   [jobs](#jobs)
*   [labels](#labels)
*   [lockbox](#lockbox)
*   [nasdevices](#nasdevices)
*   [notifications](#notifications)
*   [pools](#pools)
*   [probes](#probes)
*   [protectiongroups](#protectiongroups)
*   [protectionpolicies](#protectionpolicies)
*   [queues](#queues)
*   [recovers](#recovers)
*   [schedules](#schedules)
*   [serverconfigs](#serverconfigs)
*   [sessions](#sessions)
*   [storagenodes](#storagenodes)
*   [timepolicies](#timepolicies)
*   [vmwares](#vmwares)
*   [volumes](#volumes)

# **alerts**
## Description
This operation can be used to list the outstanding alert messages. The query parameters can be used to filter the response.

## Parameters
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th width="25%">Choices</th>
        <th width="70%">Description</th>
    </tr>
    <tr>
        <td colspan=1>state</td>
        <td width="20%">str</td>
        <td>Yes</td>
        <td></td>
        <td>
            <ul>
                <li>get</li>
            </ul>
        </td>
        <td width="80%">Select the action from the choices</td>
    </tr>
    <tr>
        <td colspan=1>query_params</td>
        <td width="20%">dict</td>
        <td>Yes</td>
        <td></td>
        <td></td>
        <td width="80%">Use this parameter to specify an "attribute matching a value" or an "attribute supports time range" on which to filter the results. Either exact match of the entered value or entered time range is supported. For Example - AttributeName:Value</td>
    </tr>
    <tr>
        <td colspan=1>field_params</td>
        <td width="20%">list</td>
        <td>Yes</td>
        <td></td>
        <td></td>
        <td width="80%">This parameter setting helps to limit the information in the response. If not specified, all the fields are shown</td>
    </tr>
</table>

## Examples
```
- name: Get Alert message and priority warning.
  dellemc.networker.alert:
    state: get
    field_params:
      - message
    query_params:
      priority: warning

- name: Get all Alert messages
  dellemc.networker.alert:
    state: get
```

## Authors
Sudarshan Kshirsagar (@kshirs1)

<div style="text-align:right"><a href="#contents">Back to Contents</a></div>


# **backups**
## Description
This operation can be used to retrieve the information about all the backups. However, the query parameters can be used to filter the response.
## Parameters
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th width="25%">Choices</th>
        <th width="70%">Description</th>
    </tr>
    <tr>
        <td colspan=1>state</td>
        <td width="20%">str</td>
        <td>Yes</td>
        <td></td>
        <td>
            <ul>
                <li>get</li>
                <li>delete</li>
            </ul>
        </td>
        <td width="80%">Select the action from the choices</td>
    </tr>
    <tr>
        <td colspan=1>backupId</td>
        <td width="20%">str</td>
        <td>No</td>
        <td></td>
        <td></td>
        <td width="80%">The attribute specifies the backup id</td>
    </tr>
    <tr>
        <td colspan=1>instanceId</td>
        <td width="20%">str</td>
        <td>No</td>
        <td></td>
        <td></td>
        <td width="80%">This attribute specifies the ID of the backup instance.</td>
    </tr>
    <tr>
        <td colspan=1>backupMountSessionId</td>
        <td width="20%">str</td>
        <td>No</td>
        <td></td>
        <td></td>
        <td width="80%">The value of mount session id in the Location Header attribute of a workers mount task.</td>
    </tr>
    <tr>
        <td colspan=1>browseSessionId</td>
        <td width="20%">str</td>
        <td>No</td>
        <td></td>
        <td></td>
        <td width="80%">Use this attribute if you want to filter the resources as per parameter values.</td>
    </tr>
    <tr>
        <td colspan=1>query_params</td>
        <td width="20%">dict</td>
        <td>Yes</td>
        <td></td>
        <td></td>
        <td width="80%">Use this parameter to specify an "attribute matching a value" or an "attribute supports time range" on which to filter the results. Either exact match of the entered value or entered time range is supported. For Example - AttributeName:Value</td>
    </tr>
    <tr>
        <td colspan=1>field_params</td>
        <td width="20%">list</td>
        <td>Yes</td>
        <td></td>
        <td></td>
        <td width="80%">This parameter setting helps to limit the information in the response. If not specified, all the fields are shown</td>
    </tr>
</table>

## Examples

```
```

## Authors
Sudarshan Kshirsagar (@kshirs1)

<div style="text-align:right"><a href="#contents">Back to Contents</a></div>

# **clients**

## Description
Use this module to add, delete Clients or folders. or modify and get information about them

## Parameters
<table>
                    <tr>
                        <th colspan=2>Parameter</th>
                        <th width="20%">Type</th>
                        <th>Required</th>
                        <th>Default</th>
                        <th width="25%">Choices</th>
                        <th width="70%">Description</th>
                    </tr><tr><td colspan=2>state</td><td width="20%">str</td><td>True</td><td>-</td><td><ul><li>create</li><li>delete</li><li>modify</li><li>get</li><li>run_backup</li><li>get_agents</li><li>get_instances</li><li>get_indexes</li><li>get_backups</li></ul></td><td width="80%">Use this option to specify action</td></tr><tr><td colspan=2>agent_type</td><td width="20%">str</td><td>No</td><td>-</td><td><ul><li>local_agent</li><li>remote_agents</li></ul></td><td width="80%">Agent Type</td></tr><tr><td colspan=2>backup_id</td><td width="20%">str</td><td>No</td><td>-</td><td></td><td width="80%">The attribute specifies the backup id.</td></tr><tr><td colspan=2>instance_id</td><td width="20%">str</td><td>No</td><td>-</td><td></td><td width="80%">This attribute specifies the ID of the backup instance.</td></tr><tr><td colspan=2>aliases</td><td width="20%">list</td><td>No</td><td>-</td><td></td><td width="80%">This is a list of aliases (nicknames) for the client machine that queries can match. If this list is empty, match on client name alone.</td></tr><tr><td colspan=2>backupCommand</td><td width="20%">str</td><td>No</td><td>-</td><td></td><td width="80%">The remote command to run to backup data for this client and save sets. This command can be used to perform pre and post backup processing and defaults to the "save" command. The value must not include a path and must start with the prefix "save" or "nsr".</td></tr><tr><td colspan=2>backupType</td><td width="20%">str</td><td>No</td><td>-</td><td></td><td width="80%">Backup Type</td></tr><tr><td colspan=2>blockBasedBackup</td><td width="20%">bool</td><td>No</td><td>-</td><td></td><td width="80%">Select this attribute to enable the image backups. Refer to the NetWorker Administration Guide for additional information about configuring block based backups.</td></tr><tr><td colspan=2>checkpointEnabled</td><td width="20%">bool</td><td>No</td><td>-</td><td></td><td width="80%">This attribute enables the support for checkpoint restart during scheduled backups. The save program performs a backup in an ordered manner and keeps track of the files saved. If save fails, it can be restarted from the point of interruption (file or directory). The ordering of the filesystems during backup may cause performance impact.</td></tr><tr><td colspan=2>clientId</td><td width="20%">str</td><td>No</td><td>-</td><td></td><td width="80%">This attribute is the clients identifier and cannot be changed.</td></tr><tr><td colspan=2>clientState</td><td width="20%">bool</td><td>No</td><td>-</td><td></td><td width="80%">Client State</td></tr><tr><td colspan=2>nasDevice</td><td width="20%">bool</td><td>No</td><td>-</td><td></td><td width="80%">Indicates client is a NAS device.</td></tr><tr><td colspan=2>ndmp</td><td width="20%">bool</td><td>No</td><td>-</td><td></td><td width="80%"> Indicates client is a NDMP client.</td></tr><tr><td colspan=2>ndmpMultiStreamsEnabled</td><td width="20%">bool</td><td>No</td><td>-</td><td></td><td width="80%"> Indicates client is to use the NDMP multistream feature.</td></tr><tr><td colspan=2>ndmpVendorInformation</td><td width="20%">list</td><td>No</td><td>-</td><td></td><td width="80%"> This attribute contains NDMP client vendor information.</td></tr><tr><td colspan=2>parallelSaveStreamsPerSaveSet</td><td width="20%">bool</td><td>No</td><td>-</td><td></td><td width="80%">Parallel save streams per save set - Enable parallel save streams per client resource save set during scheduled backup. Large save set backup time could be significantly reduced. Each save set will be backed-up with four parallel save streams by default. The default four can be changed by setting the PSS:streams_per_ss parameter in the clients save operations attribute. For example, PSS:streams_per_ss=1,*, 2,/data[1-3], 8,/data[45] will use one stream per Unix client save set entry by default but two streams for each of /data1, /data2 & /data3 and eight streams for each of /data4 & /data5. Client-supported wildcard characters can be used. The total number of active streams from all save sets at any one point in time will not exceed the clients parallelism, which is recommended to be a multiple of the default four or the largest PSS:streams_per_ss integer value if set.</td></tr><tr><td colspan=2>parallelism</td><td width="20%">str</td><td>No</td><td>-</td><td></td><td width="80%">The number of save sets to run in parallel.</td></tr><tr><td colspan=2>protectionGroups</td><td width="20%">list</td><td>No</td><td>-</td><td></td><td width="80%"> The groups this client is part of for workflow runs. The choices are defined by the set of existing groups.</td></tr><tr><td colspan=2>remoteAccessUsers</td><td width="20%">list</td><td>No</td><td>-</td><td></td><td width="80%">A list of remote users that are allowed to recover this clients files. If empty, only users logged into this machine are valid. Examples: sam@jupiter or user=sam,host=jupiter (user sam on machine jupiter), group=wheel,host=jupiter (any user in group wheel on host jupiter), jupiter or host=jupiter (any user on machine jupiter). Warning: If using the Restricted Data Zones feature it is possible to give access to someone not explicitly in the associated Restricted Data Zone. Use caution with wildcard characters.</td></tr><tr><td colspan=2>saveSets</td><td width="20%">list</td><td>No</td><td>-</td><td></td><td width="80%"> A list of the save sets to be backed up for this client with this schedule</td></tr><tr><td colspan=2>scheduledBackup</td><td width="20%">bool</td><td>No</td><td>-</td><td></td><td width="80%"> This attribute indicates if this client is enabled for scheduled backup</td></tr><tr><td colspan=2>storageNodes</td><td width="20%">list</td><td>No</td><td>-</td><td></td><td width="80%"> This is an ordered list of storage nodes for the client to use when saving its data. Its saves are directed to the first storage node that has an enabled device and a functional media daemon (nsrmmd). Keywords curphyhost and currechost can be used in this list only for virtual clients in a cluster. curphyhost indicates backups of a virtual client should go to the storage node on the physical host on which the virtual client resides. While currechost requests the required volume be mounted on the storage node where the recover operation is running. This list is also used during cloning; when a clone operation begins, the storage node from which the cloned data originates is consulted, and its "clone storage nodes" attribute is used, if present, as the save-side storage node. If not present, this list of storage nodes will be used to select the save-side storage node</td></tr><tr><td colspan=2>virtualClient</td><td width="20%">bool</td><td>No</td><td>-</td><td></td><td width="80%"> This attribute indicates whether the client is a virtual machine</td></tr><tr><td colspan=2>physicalHost</td><td width="20%">str</td><td>No</td><td>-</td><td></td><td width="80%">This attribute specifies the physical hostname, if this resource is for a virtual client. The hostname does not need to be fully-qualified, and must be less than 64 bytes. All clients sharing the same physical host must use the identical name (dont mix name formats such as short, FQDN or IP address).</td></tr><tr><td colspan=2>retentionPolicy</td><td width="20%">str</td><td>No</td><td>-</td><td></td><td width="80%"> The media policy used to define the retention time for client save sets. The existing set of management policies define the choices.</td></tr><tr><td colspan=2>indexHostname</td><td width="20%">str</td><td>No</td><td>-</td><td></td><td width="80%">This is the client entry under which the index entries will be stored. The client entry must be created and active when the index value is set.</td></tr><tr><td colspan=2>fileInactivityThreshold</td><td width="20%">str</td><td>No</td><td>-</td><td></td><td width="80%">The number of days a file has not been accessed before it is counted as inactive. A value of zero indicates that no inactivity statistics will be collected for this client.</td></tr><tr><td colspan=2>fileInactivityAlertThreshold</td><td width="20%">str</td><td>No</td><td>-</td><td></td><td width="80%">Percentage of space occupied by inactive files, exceeding which will generate a notification. A value of zero indicates that no alert will be sent for this client.</td></tr><tr><td colspan=2>checkpointGranularity</td><td width="20%">str</td><td>No</td><td>-</td><td><ul><li>Directory</li><li>File</li></ul></td><td width="80%">Checkpoint restart by file means that checkpoint will be created after each file is backed up. Due to performance degradation, this is recommended for savesets with a few large files only. Checkpoint restart by directory guarantees that checkpoint will be created after each directory is backed up. Checkpoints may be created at intermediate points depending on the number of files in the directory; however, this is not guaranteed.</td></tr><tr><td colspan=2>clientDirect</td><td width="20%">bool</td><td>No</td><td>-</td><td></td><td width="80%">A client direct backup bypasses the storage node and writes directly to the target disk device during a scheduled backup of the client. The target disk device can be a Data Domain or an Advanced File Type (AFTD) device. When enabled, client direct is attempted on the target disk. If a client direct backup is not possible, a storage node backup is attempted. This attribute is supported on 8.0 or later clients. For pre-7.6.1 clients, leave this attribute enabled (default setting). Although client direct is not supported on pre-8.0 clients, disabling this attribute may cause the backup to fail.</td></tr><tr><td colspan=2>scheduleBackup</td><td width="20%">bool</td><td>No</td><td>-</td><td></td><td width="80%">This attribute indicates if this client is enabled for scheduled backup</td></tr><tr><td colspan=2>directive</td><td width="20%">str</td><td>No</td><td>-</td><td></td><td width="80%">Directives tell the client how to backup certain files. The choices are defined by the set of existing directives.</td></tr><tr><td colspan=2>pool</td><td width="20%">str</td><td>No</td><td>-</td><td></td><td width="80%">Media pool used for data target selection during scheduled backup of the save sets specified in this client. This attribute is supported on 7.6.1 or later clients. Backup may fail on older (pre-7.6.1) clients for non-NULL value. This pool selection overrides any other pool criteria associated with the group or save set for this client.</td></tr><tr><td colspan=2>schedule</td><td width="20%">str</td><td>No</td><td>-</td><td></td><td width="80%">The schedule this client will use for backups. The choices are defined by the set of existing schedules.</td></tr><tr><td colspan=2>backupRenamedDirectories</td><td width="20%">str</td><td>No</td><td>-</td><td></td><td width="80%">This attribute enables the support of renamed directories during scheduled backups. The save program performs a lookup in the client file index to determine whether a directory has been renamed. If a directory has been renamed, all of the files and subdirectories under the directory will be backed up.</td></tr><tr><td colspan=2>remoteUser</td><td width="20%">str</td><td>No</td><td>-</td><td></td><td width="80%">The user as which to run remote commands on this client or to use to access application specific data. Each instance of a client can have a different value for the "remote user".</td></tr><tr><td colspan=2>remoteUserPassword</td><td width="20%">str</td><td>No</td><td>-</td><td></td><td width="80%"> The commands save and savefs use the password to gain access to the files being backed up, and other backup commands may use it to access application data. If a password is given, then the "remote user" attribute for the client resource must also be defined. This attribute is not used for Unix file system clients. Each instance of a client can have a different password.</td></tr><tr><td colspan=2>preCommand</td><td width="20%">str</td><td>No</td><td>-</td><td></td><td width="80%">The command that is specified here runs before the save sets for this client. The value must not include a path and must start with the prefix "save" or "nsr".</td></tr><tr><td colspan=2>postCommand</td><td width="20%">str</td><td>No</td><td>-</td><td></td><td width="80%">The command that is specified here runs after the save sets are completed for this client. The value must not include a path and must start with the prefix "save" or "nsr".</td></tr><tr><td colspan=2>saveOperations</td><td width="20%">str</td><td>No</td><td>-</td><td></td><td width="80%"> Save operation instructions of the form:KEYWORD:TOKEN=STATE. This attribute is required if Save set attribute for this client contains non-ASCII names. I18N:mode=nativepath is for NetWorker 7.4 or later clients on UNIX platforms and I18N:mode=utf8path is for pre-7.4 clients and NetWorker clients on Windows platforms.</td></tr><tr><td colspan=2>applicationInformation</td><td width="20%">str</td><td>No</td><td>-</td><td></td><td width="80%"> This attribute contains client application information.</td></tr><tr><td colspan=2>backupConfig</td><td width="20%">str</td><td>No</td><td>-</td><td></td><td width="80%">This attribute contains internal backup configuration data.</td></tr><tr><td colspan=2>jobControl</td><td width="20%">str</td><td>No</td><td>-</td><td><ul><li>endOnJobEnd</li><li>endOnProcessExit</li><li>useProcessExitCode</li></ul></td><td width="80%"> This attribute is intended to be used with custom backup scripts. It controls how savegrp and nsrjobd interpret end of a job and/or its status.</td></tr><tr><td colspan=2>ndmpMultistreamEnabled</td><td width="20%">bool</td><td>No</td><td>-</td><td></td><td width="80%"> Indicates client is to use the NDMP multistream feature.</td></tr><tr><td colspan=2>ndmpLogSuccessfulFileRecovery</td><td width="20%">bool</td><td>No</td><td>-</td><td></td><td width="80%"> Indicates logging of successfully recovered files.</td></tr><tr><td colspan=2>disableIpv6</td><td width="20%">bool</td><td>No</td><td>-</td><td></td><td width="80%">Disable IPv6 for NDMP.</td></tr><tr><td colspan=2>ndmpArrayName</td><td width="20%">bool</td><td>No</td><td>-</td><td></td><td width="80%"> In NDMP NAS array configurations, the logical name assigned to the array</td></tr><tr><td colspan=2>dataDomainBackup</td><td width="20%">bool</td><td>No</td><td>-</td><td></td><td width="80%">This setting ensures that the client data will be backed up only to DD Boost devices, even if the pool selected for the backups contains a mix of other device types.</td></tr><tr><td colspan=2>dataDomainInterface</td><td width="20%">str</td><td>No</td><td>-</td><td><ul><li>ip</li><li>fiberChannel</li><li>any</li></ul></td><td width="80%"> Choose the interface over which backup to a Data Domain device will occur. This option is meaningful only when Data Domain Backup is enabled for this client.</td></tr><tr><td colspan=2>probeResourceName</td><td width="20%">str</td><td>No</td><td>-</td><td></td><td width="80%">Probe resource name.</td></tr><tr><td colspan=2>proxyBackupType</td><td width="20%">str</td><td>No</td><td>-</td><td></td><td width="80%">Proxy method used for backups.</td></tr><tr><td colspan=2>proxyBackupHost</td><td width="20%">str</td><td>No</td><td>-</td><td></td><td width="80%">The host for proxy backup of this client.</td></tr><tr><td colspan=2>serverNetworkInterface</td><td width="20%">str</td><td>No</td><td>-</td><td></td><td width="80%">The unique hostname associated with the network interface on the server to be used for saves and recovers.</td></tr><tr><td colspan=2>priority</td><td width="20%">str</td><td>No</td><td>-</td><td></td><td width="80%">The backup priority of this client. Priority 1 is the highest, 1000 the lowest. Automated savegrps will attempt to back up clients with higher priorities before clients with lower priorities. Note that this is a hint only. Savegrp has many parameters to consider, and may choose a lower priority client while trying to balance the load.</td></tr><tr><td colspan=2>physicalClientParallelism</td><td width="20%">bool</td><td>No</td><td>-</td><td></td><td width="80%">Override the client parallelism and use the physical clients parallelism.</td></tr><tr><td colspan=2>saveSessionDistribution</td><td width="20%">str</td><td>No</td><td>-</td><td></td><td width="80%">Sets the threshold for the save session distribution. The client will distribute the save sessions to the next storage node in the storage node affinity list when the overall target sessions or max sessions of all devices on the current storage node is exceeded. The default threshold is max sessions.</td></tr><tr><td colspan=2>indexPath</td><td width="20%">str</td><td>No</td><td>-</td><td></td><td width="80%"> The path to the clients index directory on the server. This must be either an absolute path or NULL. If NULL, the index will reside in the index/clientname subdirectory of the EMC home directory .</td></tr><tr><td colspan=2>executablePath</td><td width="20%">str</td><td>No</td><td>-</td><td></td><td width="80%"> The path to the NSR executables on this client.</td></tr><tr><td colspan=2>backupTargetDisks</td><td width="20%">str</td><td>No</td><td>-</td><td></td><td width="80%">This is an ordered list of disk devices for the client to use when saving its data, without refering to the storage node lists. The options can be either adv_file or Data Domain type of devices. Note that this attribute does not apply to the client of the NetWorker server.</td></tr><tr><td colspan=2>ownerNotification</td><td width="20%">str</td><td>No</td><td>-</td><td></td><td width="80%">A notification action to send the contents of status messages to the owner/primary user of a client (e.g. savegrp completion messages).</td></tr><tr><td colspan=2>centralizedLogCollection</td><td width="20%">str</td><td>No</td><td>-</td><td></td><td width="80%">This attribute enables or disables local logs collections into the Centralized Logs Storage for this client. By default, it is enabled.</td></tr><tr><td colspan=2>recoverStorageNodes</td><td width="20%">list</td><td>No</td><td>-</td><td></td><td width="80%">This is an ordered list of storage nodes for the client to use when recovering data. Data will be recovered from the first storage node that has an enabled device on which we can mount the source volume and a functional media daemon (nsrmmd). If this attribute has no value, the clients `storage nodes will be consulted. If this attribute also has no value, then the servers storage nodes attribute will be used to select a target node for the recover operation. If the volume is already mounted, the storage node where it is mounted is used. If the recover storage node and read hostname for the jukebox are specified, the read hostname host will be used instead of the recover storage node host. Keyword currechost can be used in this list only for virtual clients in a cluster. It requests the required volume be mounted on the storage node where the recover operation is running.</td></tr><tr><td colspan=2>archiveServices</td><td width="20%">bool</td><td>No</td><td>-</td><td></td><td width="80%"> This attribute determines if archive services are available for the client.</td></tr><tr><td colspan=2>allSaveSetExpired</td><td width="20%">bool</td><td>No</td><td>-</td><td></td><td width="80%">This is an internal attribute indicates if the clients state can be set to decommssioned.</td></tr><tr><td colspan=2>nasManagementUser</td><td width="20%">str</td><td>No</td><td>-</td><td></td><td width="80%"> The user as which to run remote management commands on this NAS device. Each instance of a client can have a different value for the "NAS management user".</td></tr><tr><td colspan=2>nasManagementPassword</td><td width="20%">str</td><td>No</td><td>-</td><td></td><td width="80%">This password is used to perform management actions on a NAS device. If a password is given, then the "NAS management user" attribute for the client resource must also be defined. Each instance of a client can have a different password.</td></tr><tr><td colspan=2>nasManagementName</td><td width="20%">str</td><td>No</td><td>-</td><td></td><td width="80%"> In NAS device configurations, the management name of the device.</td></tr><tr><td colspan=2>nasFileAccessUser</td><td width="20%">str</td><td>No</td><td>-</td><td></td><td width="80%"> This user accesses the file services on a NAS device. Each instance of a client can have a different value for the NAS management user. This field is only used with Windows clients. This field is ignored with other client types.</td></tr><tr><td colspan=2>nasFileAccessPassword</td><td width="20%">str</td><td>No</td><td>-</td><td></td><td width="80%">This password is used to access the file services on a NAS device. If a password is specified, then the NAS file server user attribute for the client resource must also be defined. Each instance of a client can have a different password. This field is only used with Windows clients. This field is ignored with other client types.</td></tr><tr><td colspan=2>indexBackupContent</td><td width="20%">bool</td><td>No</td><td>-</td><td></td><td width="80%">Index files and directories on the snapshot.</td></tr><tr><td colspan=2>tags</td><td width="20%">list</td><td>No</td><td>-</td><td></td><td width="80%">This attribute contains tags for the clients</td></tr><tr><td colspan=2>comment</td><td width="20%">str</td><td>No</td><td>-</td><td></td><td width="80%">Any user defined description of this client or other explanatory remarks.</td></tr><tr><td colspan=2>name</td><td width="20%">str</td><td>No</td><td>-</td><td></td><td width="80%">This attribute is the hostname of the NSR client. It is recommended that you specify the fully qualified domain name (FQDN) of the host. For OS cluster hosts, type the FDQN of the virtual host. For application cluster hosts, type the FQDN of the application cluster host. For example, for an Oracle cluster, type the RAC hostname. For an Exchange IP DAG, type the DAG name. The application module administrator guides provide more information.</td></tr><tr><td colspan=2>query_params</td><td width="20%">dict</td><td>No</td><td>-</td><td></td><td width="80%">Use this attribute if you want to filter the resources as per parameter values.</td></tr><tr><td colspan=2>field_params</td><td width="20%">list</td><td>No</td><td>-</td><td></td><td width="80%">Use this attribute if you want to list only perticular fields</td></tr><tr><td colspan=2>resourceId</td><td width="20%">str</td><td>No</td><td>-</td><td></td><td width="80%">For each resource, resourceId is generated by networker server and this field is used to identify the resource when you want to modify the properities for it. Use this attribute if you want to modify the properties of resource after creation.</td></tr></table>

## Examples
## Authors

<div style="text-align:right"><a href="#contents">Back to Contents</a></div>

# **datadomains**
## Description
## Parameters
## Examples
## Authors

<div style="text-align:right"><a href="#contents">Back to Contents</a></div>

# **devices**
## Description
## Parameters
## Examples
## Authors

<div style="text-align:right"><a href="#contents">Back to Contents</a></div>

# **directives**
## Description
## Parameters
## Examples
## Authors

<div style="text-align:right"><a href="#contents">Back to Contents</a></div>

# **jobs**
## Description
## Parameters
## Examples
## Authors

<div style="text-align:right"><a href="#contents">Back to Contents</a></div>

# **labels**
## Description
## Parameters
## Examples
## Authors

<div style="text-align:right"><a href="#contents">Back to Contents</a></div>

# **lockbox**
## Description
## Parameters
## Examples
## Authors

<div style="text-align:right"><a href="#contents">Back to Contents</a></div>

# **nasdevices**
## Description
## Parameters
## Examples
## Authors

<div style="text-align:right"><a href="#contents">Back to Contents</a></div>

# **notifications**
## Description
## Parameters
## Examples
## Authors

<div style="text-align:right"><a href="#contents">Back to Contents</a></div>

# **pools**
## Description
## Parameters
## Examples
## Authors

<div style="text-align:right"><a href="#contents">Back to Contents</a></div>

# **probes**
## Description
## Parameters
## Examples
## Authors

<div style="text-align:right"><a href="#contents">Back to Contents</a></div>

# **protectiongroups**
## Description
## Parameters
## Examples
## Authors

<div style="text-align:right"><a href="#contents">Back to Contents</a></div>

# **protectionpolicies**
## Description
## Parameters
## Examples
## Authors

<div style="text-align:right"><a href="#contents">Back to Contents</a></div>

# **queues**
## Description
## Parameters
## Examples
## Authors

<div style="text-align:right"><a href="#contents">Back to Contents</a></div>

# **recovers**
## Description
## Parameters
## Examples
## Authors

<div style="text-align:right"><a href="#contents">Back to Contents</a></div>

# **schedules**
## Description
## Parameters
## Examples
## Authors

<div style="text-align:right"><a href="#contents">Back to Contents</a></div>

# **serverconfigs**
## Description
## Parameters
## Examples
## Authors

<div style="text-align:right"><a href="#contents">Back to Contents</a></div>

# **sessions**
## Description
## Parameters
## Examples
## Authors

<div style="text-align:right"><a href="#contents">Back to Contents</a></div>

# **storagenodes**
## Description
## Parameters
## Examples
## Authors

<div style="text-align:right"><a href="#contents">Back to Contents</a></div>

# **timepolicies**
## Description
## Parameters
## Examples
## Authors

<div style="text-align:right"><a href="#contents">Back to Contents</a></div>

# **vmwares**
## Description
## Parameters
## Examples
## Authors

<div style="text-align:right"><a href="#contents">Back to Contents</a></div>

# **volumes**
## Description
## Parameters
## Examples
## Authors

<div style="text-align:right"><a href="#contents">Back to Contents</a></div>

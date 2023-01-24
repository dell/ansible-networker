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
                <li>create</li>
                <li>delete</li>
				<li>modify</li>
				<li>get</li>
				<li>run_backup</li>
				<li>get_agents</li>
				<li>get_instances</li>
				<li>get_indexes</li>
				<li>get_backups</li>
            </ul>
        </td>
        <td width="80%">Select the action from the choices</td>
    </tr>
    <tr>
        <td colspan=1>agent_type</td>
        <td width="20%">str</td>
        <td>No</td>
        <td></td>
        <td>
            <ul>
                <li>local_agent</li>
                <li>remote_agents</li>
            </ul>
        </td>
        <td width="80%">Agent Type</td>
    </tr>
    <tr>
        <td colspan=1>backup_id</td>
        <td width="20%">str</td>
        <td>No</td>
        <td></td>
        <td></td>
        <td width="80%">The attribute specifies the backup id.</td>
    </tr>
    <tr>
        <td colspan=1>instance_id</td>
        <td width="20%">str</td>
        <td>No</td>
        <td></td>
        <td></td>
        <td width="80%">This attribute specifies the ID of the backup instance.</td>
    </tr>
    <tr>
        <td colspan=1>aliases</td>
        <td width="20%">str</td>
        <td>No</td>
        <td></td>
        <td></td>
        <td width="80%">This is a list of aliases (nicknames) for the client machine that queries can match. If this list is empty, match on client name alone.</td>
    </tr>
    <tr>
        <td colspan=1>backupCommand</td>
        <td width="20%">str</td>
        <td>No</td>
        <td></td>
        <td></td>
        <td width="80%">The remote command to run to backup data for this client and save sets. This command can be used to perform pre and post backup processing and defaults to the "save" command. The value must not include a path and must start with the prefix "save" or "nsr".</td>
    </tr>
    <tr>
        <td colspan=1>backupType</td>
        <td width="20%">str</td>
        <td>No</td>
        <td></td>
        <td></td>
        <td width="80%">Backup Type</td>
    </tr>
    <tr>
        <td colspan=1>blockBasedBackup</td>
        <td width="20%">bool</td>
        <td>No</td>
        <td></td>
        <td></td>
        <td width="80%">Select this attribute to enable the image backups. Refer to the NetWorker Administration Guide for additional information about configuring block based backups.</td>
    </tr>
    <tr>
        <td colspan=1>checkpointEnabled</td>
        <td width="20%">bool</td>
        <td>No</td>
        <td></td>
        <td></td>
        <td width="80%">This attribute enables the support for checkpoint restart during scheduled backups. The save program performs a backup in an ordered manner and keeps track of the files saved. If save fails, it can be restarted from the point of interruption (file or directory). The ordering of the filesystems during backup may cause performance impact.</td>
    </tr>
    <tr>
        <td colspan=1>clientId</td>
        <td width="20%">str</td>
        <td>No</td>
        <td></td>
        <td></td>
        <td width="80%">This attribute is the client's identifier and cannot be changed.</td>
    </tr>
    <tr>
        <td colspan=1>clientState</td>
        <td width="20%">str</td>
        <td>No</td>
        <td></td>
        <td></td>
        <td width="80%">Client State</td>
    </tr>
    <tr>
        <td colspan=1>nasDevice</td>
        <td width="20%">bool</td>
        <td>No</td>
        <td></td>
        <td></td>
        <td width="80%">Indicates client is a NAS device.</td>
    </tr>
    <tr>
        <td colspan=1>ndmp</td>
        <td width="20%">bool</td>
        <td>No</td>
        <td></td>
        <td></td>
        <td width="80%">Indicates client is a NDMP client.</td>
    </tr>
    <tr>
        <td colspan=1>ndmpMultiStreamsEnabled</td>
        <td width="20%">bool</td>
        <td>No</td>
        <td></td>
        <td></td>
        <td width="80%">Indicates client is to use the NDMP multistream feature.</td>
    </tr>
    <tr>
        <td colspan=1>ndmpVendorInformation</td>
        <td width="20%">bool</td>
        <td>No</td>
        <td></td>
        <td></td>
        <td width="80%">This attribute contains NDMP client vendor information.</td>
    </tr>
    <tr>
        <td colspan=1>parallelSaveStreamsPerSaveSet</td>
        <td width="20%">bool</td>
        <td>No</td>
        <td></td>
        <td></td>
        <td width="80%">This attribute specifies whether to enable Parallel Save Streams(PSS). Enabling PSS results in significant performance improvements due to save set aggregation.</td>
    </tr>
</table>
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

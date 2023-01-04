# Copyright ©️ 2022 Dell Inc. or its subsidiaries.
from . import nsrapi
import urllib3
urllib3.disable_warnings()


class vmwareApi():
    def __init__(self, auth=None, url=None):
        self.auth = auth
        self.url = url

    def delete_backup_v_proxy_vm_browse_session(self, vcenter_hostname, vm_uuid, backup_id, vproxy_mount_session_id,
                                                vproxy_browse_session_id):
        auth = self.auth
        url = self.url
        method = 'DELETE'
        resource_path = '/vmware/vcenters/%s/protectedvms/%s/backups/%s/op/vmmount/%s/vmbrowse/%s' % (vcenter_hostname, vm_uuid, backup_id, vproxy_mount_session_id,
                                                vproxy_browse_session_id)
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def delete_instance_v_proxy_vm_browse_session(self, vcenter_hostname, vm_uuid, backup_id, instance_id,
                                                  vproxy_mount_session_id, vproxy_browse_session_id):
        auth = self.auth
        url = self.url
        method = 'DELETE'
        resource_path = '/vmware/vcenters/%s/protectedvms/%s/backups/%s/instances/%s/op/vmmount/%s/vmbrowse/%s' % (vcenter_hostname, vm_uuid, backup_id, instance_id,
                                                  vproxy_mount_session_id, vproxy_browse_session_id)
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def delete_v_center(self, vcenter_hostname):
        auth = self.auth
        url = self.url
        method = 'DELETE'
        resource_path = '/vmware/vcenters/%s' % vcenter_hostname
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def delete_v_proxy(self, vproxy_hostname):
        auth = self.auth
        url = self.url
        method = 'DELETE'
        resource_path = '/vmware/vproxies/%s' % vproxy_hostname
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def get_backup_v_proxy_vm_browse_session_contents(self, vcenter_hostname, vm_uuid, backup_id,
                                                      vproxy_mount_session_id, vproxy_browse_session_id):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/vmware/vcenters/%s/protectedvms/%s/backups/%s/op/vmmount/%s/vmbrowse/%s/contents' % (vcenter_hostname, vm_uuid, backup_id,
                                                      vproxy_mount_session_id, vproxy_browse_session_id)
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def get_backup_v_proxy_vm_browse_session_response(self, vcenter_hostname, vm_uuid, backup_id,
                                                      vproxy_mount_session_id, vproxy_browse_session_id):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/vmware/vcenters/%s/protectedvms/%s/backups/%s/op/vmmount/%s/vmbrowse/%s' % (vcenter_hostname, vm_uuid, backup_id,
                                                      vproxy_mount_session_id, vproxy_browse_session_id)
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def get_backup_v_proxy_vm_browse_session_response_list(self, vcenter_hostname, vm_uuid, backup_id,
                                                           vproxy_mount_session_id):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/vmware/vcenters/%s/protectedvms/%s/backups/%s/op/vmmount/%s/vmbrowse' % (vcenter_hostname, vm_uuid, backup_id, vproxy_mount_session_id)
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def get_backup_v_proxy_vm_mount_session_response(self, vcenter_hostname, vm_uuid, backup_id,
                                                     vproxy_mount_session_id):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/vmware/vcenters/%s/protectedvms/%s/backups/%s/op/vmmount/%s' % (vcenter_hostname, vm_uuid, backup_id,
                                                     vproxy_mount_session_id)
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def get_instance_v_proxy_vm_browse_session_contents(self, vcenter_hostname, vm_uuid, backup_id, instance_id,
                                                        vproxy_mount_session_id, vproxy_browse_session_id):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/vmware/vcenters/%s/protectedvms/%s/backups/%s/instances/%s/op/vmmount/%s/vmbrowse/%s/contents' % (vcenter_hostname, vm_uuid, backup_id, instance_id,
                                                        vproxy_mount_session_id, vproxy_browse_session_id)
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def get_instance_v_proxy_vm_browse_session_response(self, vcenter_hostname, vm_uuid, backup_id, instance_id,
                                                        vproxy_mount_session_id, vproxy_browse_session_id):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/vmware/vcenters/%s/protectedvms/%s/backups/%s/instances/%s/op/vmmount/%s/vmbrowse/%s' % (vcenter_hostname, vm_uuid, backup_id, instance_id,
                                                        vproxy_mount_session_id, vproxy_browse_session_id)
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def get_instance_v_proxy_vm_browse_session_response_list(self, vcenter_hostname, vm_uuid, backup_id, instance_id,
                                                             vproxy_mount_session_id):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/vmware/vcenters/%s/protectedvms/%s/backups/%s/instances/%s/op/vmmount/%s/vmbrowse' % (vcenter_hostname, vm_uuid, backup_id, instance_id,
                                                             vproxy_mount_session_id)
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def get_instance_v_proxy_vm_mount_session_response(self, vcenter_hostname, vm_uuid, backup_id, instance_id,
                                                       vproxy_mount_session_id):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/vmware/vcenters/%s/protectedvms/%s/backups/%s/instances/%s/op/vmmount/%s' % (vcenter_hostname, vm_uuid, backup_id, instance_id,
                                                       vproxy_mount_session_id)
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def get_v_center(self, vcenter_hostname):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/vmware/vcenters/%s' % vcenter_hostname
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def get_v_center_protected_vm(self, vcenter_hostname, vm_uuid):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/vmware/vcenters/%s/protectedvms/%s' % (vcenter_hostname, vm_uuid)
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def get_v_center_protected_vm_backup_instances(self, vcenter_hostname, vm_uuid, backup_id):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/vmware/vcenters/%s/protectedvms/%s/backups/%s/instances' % (vcenter_hostname, vm_uuid, backup_id)
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def get_v_center_protected_vm_backups(self, vcenter_hostname, vm_uuid):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/vmware/vcenters/%s/protectedvms/%s/backups' % (vcenter_hostname, vm_uuid)
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def get_v_center_protected_vms(self, vcenter_hostname):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/vmware/vcenters/%s/protectedvms' % vcenter_hostname
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def get_v_center_vm(self, vcenter_hostname, vm_uuid):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/vmware/vcenters/%s/vms/%s' % (vcenter_hostname, vm_uuid)
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def get_v_center_vms(self, vcenter_hostname):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/vmware/vcenters/%s/vms' % (vcenter_hostname)
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def get_v_centers(self):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/vmware/vcenters'
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def get_v_mware_protected_vms(self):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/vmware/protectedvms'
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response
    
    def get_v_mware_v_center_vm_protection_details(self, vcenter_hostname, vm_uuid):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/vmware/vcenters/%s/vms/%s/protectiondetails' % (vcenter_hostname, vm_uuid)
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response  

    def get_v_mware_vms(self):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/vmware/vms'
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response
        
    def get_v_proxies(self):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/vmware/vproxies'
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def get_v_proxy(self, vproxy_hostname):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/vmware/vproxies/%s' % vproxy_hostname
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def get_v_proxy_redeploy(self, id):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/vmware/vproxies/%s/op/redeployment' % (id)
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def post_backup_v_proxy_vm_browse_session_request(self, body, vcenter_hostname, vm_uuid,
                                                      backup_id, vproxy_mount_session_id):
        auth = self.auth
        url = self.url
        method = 'POST'
        resource_path = '/vmware/vcenters/%s/protectedvms/%s/backups/%s/op/vmmount/%s/vmbrowse' % (vcenter_hostname, vm_uuid,
                                                      backup_id, vproxy_mount_session_id)
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response
        
    def post_instance_v_proxy_vm_browse_session_request(self, body, vcenter_hostname, vm_uuid,
                                                        backup_id, instance_id, vproxy_mount_session_id):
        auth = self.auth
        url = self.url
        method = 'POST'
        resource_path = '/vmware/vcenters/%s/protectedvms/%s/backups/%s/instances/%s/op/vmmount/%s/vmbrowse' % (vcenter_hostname, vm_uuid,
                                                        backup_id, instance_id, vproxy_mount_session_id)
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def post_op_register_v_proxy(self, body):
        auth = self.auth
        url = self.url
        method = 'POST'
        resource_path = '/vmware/vproxies/op/register' 
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response
        
    def post_v_center(self, body):
        auth = self.auth
        url = self.url
        method = 'POST'
        resource_path = '/vmware/vcenters'
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response
        
    def post_v_center_op_refresh(self, vcenter_hostname):
        auth = self.auth
        url = self.url
        method = 'POST'
        body = None
        resource_path = '/vmware/vcenters/%s/op/refresh' % (vcenter_hostname)
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response  

    def post_v_center_plugin(self, body, vcenter_hostname):
        auth = self.auth
        url = self.url
        method = 'POST'
        resource_path = '/vmware/vcenters/%s/plugins' % vcenter_hostname
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response
        
    def post_v_center_protected_vm_backup_inspect_backup(self, vcenter_hostname, vm_uuid, backup_id):
        auth = self.auth
        url = self.url
        method = 'POST'
        body = None
        resource_path = '/vmware/vcenters/%s/protectedvms/%s/backups/%s/op/inspectbackup' % (vcenter_hostname, vm_uuid, backup_id)
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response
        
    def post_v_center_protected_vm_backup_instance_inspect_backup(self, vcenter_hostname, vm_uuid,
                                                                  backup_id, instance_id):
        auth = self.auth
        url = self.url
        method = 'POST'
        body = None
        resource_path = '/vmware/vcenters/%s/protectedvms/%s/backups/%s/instances/%s/op/inspectbackup' % (vcenter_hostname, vm_uuid,
                                                                  backup_id, instance_id)
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response     

    def post_v_center_protected_vm_backup_instance_recover(self, body, vcenter_hostname, vm_uuid,
                                                           backup_id, instance_id):
        auth = self.auth
        url = self.url
        method = 'POST'
        resource_path = '/vmware/vcenters/%s/protectedvms/%s/backups/%s/instances/%s/op/recover' % (vcenter_hostname, vm_uuid,
                                                           backup_id, instance_id)
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def post_v_center_protected_vm_backup_instance_vm_mount(self, body, vcenter_hostname, vm_uuid,
                                                            backup_id, instance_id):
        auth = self.auth
        url = self.url
        method = 'POST'
        resource_path = '/vmware/vcenters/%s/protectedvms/%s/backups/%s/instances/%s/op/vmmount' % (vcenter_hostname, vm_uuid,
                                                            backup_id, instance_id)
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def post_v_center_protected_vm_backup_recover(self, body, vcenter_hostname, vm_uuid, backup_id):

        auth = self.auth
        url = self.url
        method = 'POST'
        resource_path = '/vmware/vcenters/%s/protectedvms/%s/backups/%s/op/recover' % (vcenter_hostname, vm_uuid, backup_id)
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def post_v_center_protected_vm_backup_vm_mount(self, body, vcenter_hostname, vm_uuid, backup_id):
        auth = self.auth
        url = self.url
        method = 'POST'
        resource_path = '/vmware/vcenters/%s/protectedvms/%s/backups/%s/op/vmmount' % (vcenter_hostname, vm_uuid, backup_id)
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def post_v_mware_op_refresh_v_centers(self):
        auth = self.auth
        url = self.url
        method = 'POST'
        body = None
        resource_path = '/vmware/op/refreshvcenters'
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def post_v_mware_v_center_vm_op_backup(self, body, vcenter_hostname, vm_uuid):
        auth = self.auth
        url = self.url
        method = 'POST'
        resource_path = '/vmware/vcenters/%s/vms/%s/op/backup' %(vcenter_hostname, vm_uuid)
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def post_v_proxy(self, body):
        auth = self.auth
        url = self.url
        method = 'POST'
        resource_path = '/vmware/vproxies'
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def post_v_proxy_redeploy(self, body, id):
        auth = self.auth
        url = self.url
        method = 'POST'
        resource_path = '/vmware/vproxies/%s/op/redeployment' % (id)
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def put_backup_v_proxy_vm_browse_session_request(self, body, vcenter_hostname, vm_uuid, backup_id,
                                                     vproxy_mount_session_id, vproxy_browse_session_id):
        auth = self.auth
        url = self.url
        method = 'PUT'
        resource_path = '/vmware/vcenters/%s/protectedvms/%s/backups/%s/op/vmmount/%s/vmbrowse/%s' % (vcenter_hostname, vm_uuid, backup_id,
                                                     vproxy_mount_session_id, vproxy_browse_session_id)
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def put_instance_v_proxy_vm_browse_session_request(self, body, vcenter_hostname, vm_uuid,
                                                       backup_id, instance_id, vproxy_mount_session_id,
                                                       vproxy_browse_session_id):
        auth = self.auth
        url = self.url
        method = 'PUT'
        resource_path = '/vmware/vcenters/%s/protectedvms/%s/backups/%s/instances/%s/op/vmmount/%s/vmbrowse/%s' % (vcenter_hostname, vm_uuid,
                                                       backup_id, instance_id, vproxy_mount_session_id,
                                                       vproxy_browse_session_id)
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def put_v_center(self, body, vcenter_hostname):
        auth = self.auth
        url = self.url
        method = 'PUT'
        resource_path = '/vmware/vcenters/%s' % vcenter_hostname
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def put_v_proxy(self, body, vproxy_hostname):
        auth = self.auth
        url = self.url
        method = 'PUT'
        resource_path = '/vmware/vproxies/%s' % vproxy_hostname
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def put_vm_backup(self, body, vcenter_hostname, vm_uuid, backup_id):
        auth = self.auth
        url = self.url
        method = 'PUT'
        resource_path = '/vmware/vcenters/%s/protectedvms/%s/backups/%s' % (vcenter_hostname, vm_uuid, backup_id)
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response



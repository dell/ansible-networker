# Copyright ©️ 2022 Dell Inc. or its subsidiaries.
from . import nsrapi
import urllib3
urllib3.disable_warnings()


class BackupsApi():
    def __init__(self, auth=None, url=None):
        self.auth = auth
        self.url = url

    def delete_backup(self, backup_id):
        auth = self.auth
        url = self.url
        method = 'DELETE'
        resource_path = '/backups/%s' % backup_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def delete_backup_instance(self, backup_id, instance_id):
        auth = self.auth
        url = self.url
        method = 'DELETE'
        resource_path = '/backups/%s/instances/%s' % (backup_id, instance_id)
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def delete_backup_mount_session(self, backup_id, backup_mount_session_id):
        auth = self.auth
        url = self.url
        method = 'DELETE'
        resource_path = '/backups/%s/op/mount/%s' % (backup_id, backup_mount_session_id)
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def get_backup(self, backup_id):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/backups/%s' % backup_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def get_backup_browse_session_contents(self, backup_id, backup_mount_session_id, browse_session_id):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/backups/%s/op/mount/%s/browse/%s/contents' % (backup_id, backup_mount_session_id, browse_session_id)
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def get_backup_instance(self, backup_id, instance_id):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/backups/%s/instances/%s' % (backup_id, instance_id)
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def get_backup_instances(self, backup_id):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/backups/%s/instances' % backup_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def get_backup_mount_session(self, backup_id, backup_mount_session_id):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/backups/%s/op/mount/%s' % (backup_id, backup_mount_session_id)
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def get_backups(self, query_params, field_params):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/backups'
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path,
                               query_params=query_params, field_params=field_params)
        api_response = nsrApi.request()
        return api_response

    def post_backup_browse_session_request(self, body, backup_id, backup_mount_session_id):
        auth = self.auth
        url = self.url
        method = 'POST'
        resource_path = '/backups/%s/op/mount/%s/browse' % (backup_id, backup_mount_session_id)
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def post_backup_op_mount(self, body, backup_id):
        auth = self.auth
        url = self.url
        method = 'POST'
        resource_path = '/backups/%s/op/mount' % backup_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def put_backup(self, body, backup_id):
        auth = self.auth
        url = self.url
        method = 'PUT'
        resource_path = '/backups/%s' % backup_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

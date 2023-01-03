# Copyright ©️ 2022 Dell Inc. or its subsidiaries.
import os.path as path
import sys
from . import nsrapi
import urllib3
urllib3.disable_warnings()


class ServerApi():
    def __init__(self, auth=None, url=None):
        self.auth = auth
        self.url = url

    def get_server_configs(self):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/serverconfig'
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def put_server_config(self, body):
        auth = self.auth
        url = self.url
        method = 'PUT'
        resource_path = '/serverconfig'
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def delete_user_group(self, usergroup_id):
        auth = self.auth
        url = self.url
        method = 'DELETE'
        resource_path = '/usergroups/%s' % usergroup_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def get_user_group(self, usergroup_id):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/usergroups/%s' % usergroup_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def get_user_groups(self):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/usergroups'
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def post_user_group(self, body):
        auth = self.auth
        url = self.url
        method = 'POST'
        resource_path = '/usergroups'
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def put_user_group(self, usergroup_id, body):
        auth = self.auth
        url = self.url
        method = 'PUT'
        resource_path = '/usergroups/%s' % usergroup_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def get_audit_log_configs(self):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/auditlogconfig'
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def put_audit_log_config(self, body):
        auth = self.auth
        url = self.url
        method = 'PUT'
        resource_path = '/auditlogconfig'
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def get_server_messages(self):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/servermessages'
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def get_server_statistics(self):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/serverstatistics'
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

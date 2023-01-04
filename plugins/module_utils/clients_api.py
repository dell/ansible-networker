# Copyright ©️ 2022 Dell Inc. or its subsidiaries.
import os.path as path
import sys
from . import nsrapi
import urllib3
urllib3.disable_warnings()


class ClientsApi():
    def __init__(self, auth=None, url=None):
        self.auth = auth
        self.url = url

    def get_client(self, client_id, field_params):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/clients/%s' % client_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, field_params=field_params)
        api_response = nsrApi.request()
        return api_response

    def get_clients(self, query_params, field_params):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/clients'
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path,
                               query_params=query_params, field_params=field_params)
        api_response = nsrApi.request()
        return api_response

    def put_client(self, body, client_id):
        auth = self.auth
        url = self.url
        method = 'PUT'
        resource_path = '/clients/%s' % client_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def post_client(self, body):
        auth = self.auth
        url = self.url
        method = 'POST'
        resource_path = '/clients'
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def delete_client(self, client_id):
        auth = self.auth
        url = self.url
        method = 'DELETE'
        resource_path = '/clients/%s' % client_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def client_op_backup(self, body, client_id):
        auth = self.auth
        url = self.url
        method = 'POST'
        resource_path = '/clients/%s/op/backup' % client_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def get_client_agents(self, client_id):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/clients/%s/agents' % client_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def get_client_backup(self, client_id, backup_id):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/clients/%s/backups/%s' % (client_id, backup_id)
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def get_client_backup_instance(self, client_id, backup_id, instance_id):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/clients/%s/backups/%s/instances/%s' % (client_id, backup_id, instance_id)
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def get_client_backup_instances(self, client_id, backup_id):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/clients/%s/backups/%s/instances' % (client_id, backup_id)
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def get_client_backups(self, client_id):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/clients/%s/backups' % (client_id)
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def get_client_indexes(self, client_id):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/clients/%s/indexes' % (client_id)
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def get_client_local_agents(self, client_id):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/clients/%s/agents/localagent' % (client_id)
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def get_client_remote_agents(self, client_id):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/clients/%s/agents/remoteagents' % (client_id)
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def put_client_backup(self, body, client_id, backup_id):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/clients/%s/backups/%s' % (client_id, backup_id)
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

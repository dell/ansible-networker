# Copyright ©️ 2022 Dell Inc. or its subsidiaries.
import os.path as path
import sys
from . import nsrapi
import urllib3
urllib3.disable_warnings()


class ProtectionGroupApi():
    def __init__(self, auth=None, url=None):
        self.auth = auth
        self.url = url

    def get_protection_groups(self, field_params, query_params):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/protectiongroups'
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, field_params=field_params,
                               query_params=query_params)
        api_response = nsrApi.request()
        return api_response

    def get_protection_group(self, protectionGroupId, field_params):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/protectiongroups/%s' % protectionGroupId
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, field_params=field_params)
        api_response = nsrApi.request()
        return api_response

    def put_protection_groups(self, body, protectionGroupId):
        auth = self.auth
        url = self.url
        method = 'PUT'
        resource_path = '/protectiongroups/%s' % protectionGroupId
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def delete_protection_group(self, protectionGroupId):
        auth = self.auth
        url = self.url
        method = 'DELETE'
        resource_path = '/protectiongroups/%s' % protectionGroupId
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def post_protection_groups(self, body):
        auth = self.auth
        url = self.url
        method = 'POST'
        resource_path = '/protectiongroups'
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def update_v_mware_work_items(self, body, protectionGroupId):
        auth = self.auth
        url = self.url
        method = 'POST'
        resource_path = '/protectiongroups/%s' % protectionGroupId
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

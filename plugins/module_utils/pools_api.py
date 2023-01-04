# Copyright ©️ 2022 Dell Inc. or its subsidiaries.
import os.path as path
import sys
from . import nsrapi
import urllib3
urllib3.disable_warnings()


class PoolsApi():
    def __init__(self, auth=None, url=None):
        self.auth = auth
        self.url = url

    def get_pool(self, pool_id, field_params):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/pools/%s' % pool_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, field_params=field_params)
        api_response = nsrApi.request()
        return api_response

    def get_pools(self, field_params, query_params):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/pools'
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path,
                               field_params=field_params, query_params=query_params)
        api_response = nsrApi.request()
        return api_response

    def put_pool(self, body, pool_id):
        auth = self.auth
        url = self.url
        method = 'PUT'
        resource_path = '/pools/%s' % pool_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def post_pool(self, body):
        auth = self.auth
        url = self.url
        method = 'POST'
        resource_path = '/pools'
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def delete_pool(self, pool_id):
        auth = self.auth
        url = self.url
        method = 'DELETE'
        resource_path = '/pools/%s' % pool_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

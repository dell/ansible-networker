# Copyright ©️ 2022 Dell Inc. or its subsidiaries.
import os.path as path
import sys
from . import nsrapi
import urllib3
urllib3.disable_warnings()


class ProbesApi():
    def __init__(self, auth=None, url=None):
        self.auth = auth
        self.url = url

    def delete_probe(self, probe_id):
        auth = self.auth
        url = self.url
        method = 'DELETE'
        resource_path = '/probes/%s' % probe_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def get_probe(self, probe_id):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/probes/%s' % probe_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def get_probes(self, query_params, field_params):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/probes'
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path,
                               query_params=query_params, field_params=field_params)
        api_response = nsrApi.request()
        return api_response

    def post_probe(self, body):
        auth = self.auth
        url = self.url
        method = 'POST'
        resource_path = '/probes'
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def put_probe(self, body, probe_id):
        auth = self.auth
        url = self.url
        method = 'PUT'
        resource_path = '/probes/%s' % probe_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

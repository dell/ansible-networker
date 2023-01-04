# Copyright ©️ 2022 Dell Inc. or its subsidiaries.
import os.path as path
import sys
from . import nsrapi
import urllib3
urllib3.disable_warnings()


class TimePoliciessApi():
    def __init__(self, auth=None, url=None):
        self.auth = auth
        self.url = url

    def get_timepolicy(self, timepolicy_id, field_params):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/timepolicies/%s' % timepolicy_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, field_params=field_params)
        api_response = nsrApi.request()
        return api_response

    def get_timepolicies(self, field_params, query_params):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/timepolicies'
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, field_params=field_params,
                               query_params=query_params)
        api_response = nsrApi.request()
        return api_response

    def put_timepolicy(self, body, timepolicy_id):
        auth = self.auth
        url = self.url
        method = 'PUT'
        resource_path = '/timepolicies/%s' % timepolicy_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def post_timepolicy(self, body):
        auth = self.auth
        url = self.url
        method = 'POST'
        resource_path = '/timepolicies'
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def delete_timepolicy(self, timepolicy_id):
        auth = self.auth
        url = self.url
        method = 'DELETE'
        resource_path = '/timepolicies/%s' % timepolicy_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

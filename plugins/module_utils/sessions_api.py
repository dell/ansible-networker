# Copyright ©️ 2022 Dell Inc. or its subsidiaries.
import os.path as path
import sys
from . import nsrapi
import urllib3
urllib3.disable_warnings()


class sessionsApi():
    def __init__(self, auth=None, url=None):
        self.auth = auth
        self.url = url

    def get_session(self, session_id):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/sessions/%s' % session_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def get_sessions(self, query_params, field_params):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/sessions'
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path,
                               query_params=query_params, field_params=field_params)
        api_response = nsrApi.request()
        return api_response

    def post_sessions(self, session_id, body):
        auth = self.auth
        url = self.url
        method = 'POST'
        resource_path = '/sessions/%s/op/cancel' % session_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response


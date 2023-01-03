# Copyright ©️ 2022 Dell Inc. or its subsidiaries.
from . import nsrapi
import urllib3
urllib3.disable_warnings()


class DirectivesApi():
    def __init__(self, auth=None, url=None):
        self.auth = auth
        self.url = url

    def get_directives(self, query_params, field_params):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/directives'
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path,
                               query_params=query_params, field_params=field_params)
        api_response = nsrApi.request()
        return api_response

    def delete_directive(self, directive_id):
        auth = self.auth
        url = self.url
        method = 'DELETE'
        resource_path = '/directives/%s' % directive_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def get_directive(self, directive_id, field_params):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/directives/%s' % directive_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path,
                               field_params=field_params)
        api_response = nsrApi.request()
        return api_response

    def post_directives(self, body):
        auth = self.auth
        url = self.url
        method = 'POST'
        resource_path = '/directives'
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def put_directive(self, body, directive_id):
        auth = self.auth
        url = self.url
        method = 'PUT'
        resource_path = '/directives/%s' % directive_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

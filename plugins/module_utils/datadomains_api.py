# Copyright ©️ 2022 Dell Inc. or its subsidiaries.
import os.path as path
import sys
from . import nsrapi
import urllib3
urllib3.disable_warnings()


class DatadomainApi():
    def __init__(self, auth=None, url=None):
        self.auth = auth
        self.url = url

    def delete_data_domain_system(self, data_domain_system_id):
        auth = self.auth
        url = self.url
        method = 'DELETE'
        resource_path = '/datadomainsystems/%s' % data_domain_system_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def get_data_domain_systems(self, query_params, field_params):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/datadomainsystems'
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path,
                               field_params=field_params, query_params=query_params)
        api_response = nsrApi.request()
        return api_response

    def get_data_domain_system(self, data_domain_system_id, field_params):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/datadomainsystems/%s' % data_domain_system_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, field_params=field_params)
        api_response = nsrApi.request()
        return api_response

    def post_data_domain(self, body):
        auth = self.auth
        url = self.url
        method = 'POST'
        resource_path = '/datadomainsystems'
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def post_op_create_folder(self, body, data_domain_system_id):
        auth = self.auth
        url = self.url
        method = 'POST'
        resource_path = '/datadomainsystems/%s/op/createfolder' % data_domain_system_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def post_op_create_unit(self, body, data_domain_system_id):
        auth = self.auth
        url = self.url
        method = 'POST'
        resource_path = '/datadomainsystems/%s/op/createunit' % data_domain_system_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def post_op_delete_folder(self, body, data_domain_system_id):
        auth = self.auth
        url = self.url
        method = 'POST'
        resource_path = '/datadomainsystems/%s/op/deletefolder' % data_domain_system_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def post_op_delete_storage_unit(self, body, data_domain_system_id):
        auth = self.auth
        url = self.url
        method = 'POST'
        resource_path = '/datadomainsystems/%s/op/deleteunit' % data_domain_system_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def post_op_list_folders(self, body, data_domain_system_id):
        auth = self.auth
        url = self.url
        method = 'POST'
        resource_path = '/datadomainsystems/%s/op/listfolders' % data_domain_system_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def post_op_list_units(self, body, data_domain_system_id):
        auth = self.auth
        url = self.url
        method = 'POST'
        resource_path = '/datadomainsystems/%s/op/listunits' % data_domain_system_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def post_op_read_folder(self, body, data_domain_system_id):
        auth = self.auth
        url = self.url
        method = 'POST'
        resource_path = '/datadomainsystems/%s/op/readfolder' % data_domain_system_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def post_op_read_unit(self, body, data_domain_system_id):
        auth = self.auth
        url = self.url
        method = 'POST'
        resource_path = '/datadomainsystems/%s/op/readunit' % data_domain_system_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def put_data_domain_system(self, body, data_domain_system_id):
        auth = self.auth
        url = self.url
        method = 'PUT'
        resource_path = '/datadomainsystems/%s' % data_domain_system_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

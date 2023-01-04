# Copyright ©️ 2022 Dell Inc. or its subsidiaries.
import os.path as path
import sys
from . import nsrapi
import urllib3
urllib3.disable_warnings()


class DevicesApi():
    def __init__(self, auth=None, url=None):
        self.auth = auth
        self.url = url

    def get_device(self, device_id, field_params):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/devices/%s' % device_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path,
                               field_params=field_params)
        api_response = nsrApi.request()
        return api_response

    def get_devices(self, field_params, query_params):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/devices'
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path,
                               field_params=field_params, query_params=query_params)
        api_response = nsrApi.request()
        return api_response
    
    def get_device_op_status(self, device_id):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/devices/%s/opstatus' % device_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def put_device(self, body, device_id):
        auth = self.auth
        url = self.url
        method = 'PUT'
        resource_path = '/devices/%s' % device_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def post_device(self, body):
        auth = self.auth
        url = self.url
        method = 'POST'
        resource_path = '/devices'
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def delete_device(self, device_id):
        auth = self.auth
        url = self.url
        method = 'DELETE'
        resource_path = '/devices/%s' % device_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def post_device_op_erase(self, body, device_id):
        auth = self.auth
        url = self.url
        method = 'POST'
        resource_path = '/devices/%s/op/erase' % device_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def post_device_op_label(self, body, device_id):
        auth = self.auth
        url = self.url
        method = 'POST'
        resource_path = '/devices/%s/op/label'% device_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def post_device_op_mount(self, body, device_id):
        auth = self.auth
        url = self.url
        method = 'POST'
        resource_path = '/devices/%s/op/mount' % device_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def post_device_op_unmount(self, body, device_id):
        auth = self.auth
        url = self.url
        method = 'POST'
        resource_path = '/devices/%s/op/unmount' % device_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def post_device_op_verify_label(self, body, device_id):
        auth = self.auth
        url = self.url
        method = 'POST'
        resource_path = '/devices/%s/op/verifylabel' % device_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

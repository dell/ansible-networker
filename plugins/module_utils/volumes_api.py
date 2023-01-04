# Copyright ©️ 2022 Dell Inc. or its subsidiaries.
import os.path as path
import sys
from . import nsrapi
import urllib3
urllib3.disable_warnings()


class VolumeApi():
    def __init__(self, auth=None, url=None):
        self.auth = auth
        self.url = url

    def get_volume(self, volume_id, field_params):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/volumes/%s' % volume_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, field_params=field_params)
        api_response = nsrApi.request()
        return api_response

    def get_volumes(self, field_params, query_params):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/volumes'
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, field_params=field_params,
                               query_params=query_params)
        api_response = nsrApi.request()
        return api_response

    def post_remove_volume_from_file_index(self, volume_id, body):
        auth = self.auth
        url = self.url
        method = 'POST'
        resource_path = '/volumes/%s/op/indexpurge' % volume_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def post_change_volume_location(self, volume_id, body):
        auth = self.auth
        url = self.url
        method = 'POST'
        resource_path = '/volumes/%s/op/location' % volume_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def post_apply_recycle_policy_volume(self, volume_id, body):
        auth = self.auth
        url = self.url
        method = 'POST'
        resource_path = '/volumes/%s/op/recycle' % volume_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def post_mark_scan_required_volume(self, volume_id, body):
        auth = self.auth
        url = self.url
        method = 'POST'
        resource_path = '/volumes/%s/op/scan' % volume_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def post_change_mode_volume(self, volume_id, body):
        auth = self.auth
        url = self.url
        method = 'POST'
        resource_path = '/volumes/%s/op/state' % volume_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def delete_volume(self, volume_id):
        auth = self.auth
        url = self.url
        method = 'DELETE'
        resource_path = '/volumes/%s' % volume_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

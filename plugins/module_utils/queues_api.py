# Copyright ©️ 2022 Dell Inc. or its subsidiaries.
from . import nsrapi
import urllib3
urllib3.disable_warnings()


class QueuessApi():
    def __init__(self, auth=None, url=None):
        self.auth = auth
        self.url = url

    def get_queue(self, queue_id):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/queue/%s' % queue_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

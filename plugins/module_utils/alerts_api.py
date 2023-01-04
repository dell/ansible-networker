# Copyright ©️ 2022 Dell Inc. or its subsidiaries.
from . import nsrapi
import urllib3
urllib3.disable_warnings()


class AlertsApi():
    def __init__(self, auth=None, url=None):
        self.auth = auth
        self.url = url

    def get_alerts(self, query_params, field_params):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/alerts'
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path,
                               query_params=query_params, field_params=field_params)
        api_response = nsrApi.request()
        return api_response

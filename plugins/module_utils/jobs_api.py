# Copyright ©️ 2022 Dell Inc. or its subsidiaries.
from . import nsrapi
import urllib3
urllib3.disable_warnings()


class JobsApi():
    def __init__(self, auth=None, url=None):
        self.auth = auth
        self.url = url

    def get_jobs(self, query_params, field_params):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/jobs'
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path,
                               query_params=query_params, field_params=field_params)
        api_response = nsrApi.request()
        return api_response

    def get_job(self, job_id, field_params):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/jobs/%s' % job_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, field_params=field_params)
        api_response = nsrApi.request()
        return api_response

    def get_job_group(self, job_group_id, field_params):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/jobgroups/%s' % job_group_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path,
                               field_params=field_params)
        api_response = nsrApi.request()
        return api_response

    def get_job_groups(self, field_params, query_params):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/jobgroups'
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path,
                               field_params=field_params, query_params=query_params)
        api_response = nsrApi.request()
        return api_response

    def get_job_indications(self, field_params, query_params):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/jobindications'
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path,
                               field_params=field_params, query_params=query_params)
        api_response = nsrApi.request()
        return api_response

    def get_job_log(self, job_id, field_params):
        auth = self.auth
        url = self.url
        headers = ''
        method = 'GET'
        resource_path = '/jobs/%s/log' % job_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path,
                               field_params=field_params, headers=headers)
        api_response = nsrApi.request()
        return api_response

    def post_job_op_cancel(self, body, job_id):
        auth = self.auth
        url = self.url
        method = 'POST'
        resource_path = '/jobs/%s/op/cancel' % job_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path,
                               body=body)
        api_response = nsrApi.request()
        return api_response

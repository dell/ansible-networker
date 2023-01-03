# Copyright ©️ 2022 Dell Inc. or its subsidiaries.
from . import nsrapi
import urllib3
urllib3.disable_warnings()


class ProtectionpoliciesApi():
    def __init__(self, auth=None, url=None):
        self.auth = auth
        self.url = url

    def delete_policy(self, policy_id):
        auth = self.auth
        url = self.url
        method = 'DELETE'
        resource_path = '/protectionpolicies/%s' % policy_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def delete_policy_workflow(self, policy_id, workflow_id):
        auth = self.auth
        url = self.url
        method = 'DELETE'
        resource_path = '/protectionpolicies/%s/workflows/%s' % (policy_id, workflow_id)
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path)
        api_response = nsrApi.request()
        return api_response

    def get_policies(self, field_params, query_params):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/protectionpolicies'
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, field_params=field_params,
                               query_params=query_params)
        api_response = nsrApi.request()
        return api_response

    def get_policy(self, policy_id, field_params):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/protectionpolicies/%s' % policy_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, field_params=field_params)
        api_response = nsrApi.request()
        return api_response

    def get_policy_workflow(self, policy_id, workflow_id, field_params):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/protectionpolicies/%s/workflows/%s' % (policy_id, workflow_id)
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, field_params=field_params)
        api_response = nsrApi.request()
        return api_response

    def get_policy_workflows(self, policy_id, field_params, query_params):
        auth = self.auth
        url = self.url
        method = 'GET'
        resource_path = '/protectionpolicies/%s/workflows' % (policy_id)
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path,
                               field_params=field_params, query_params=query_params)
        api_response = nsrApi.request()
        return api_response

    def post_policy(self, body):
        auth = self.auth
        url = self.url
        method = 'POST'
        resource_path = '/protectionpolicies'
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def post_policy_workflow(self, body, policy_id):
        auth = self.auth
        url = self.url
        method = 'POST'
        resource_path = '/protectionpolicies/%s/workflows' % policy_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def put_policy(self, body, policy_id):
        auth = self.auth
        url = self.url
        method = 'PUT'
        resource_path = '/protectionpolicies/%s' % policy_id
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

    def put_policy_workflow(self, body, policy_id, workflow_id):
        auth = self.auth
        url = self.url
        method = 'PUT'
        resource_path = '/protectionpolicies/%s/workflows/%s' % (policy_id, workflow_id)
        nsrApi = nsrapi.nsrApi(method=method, auth=auth, url=url, resource_path=resource_path, body=body)
        api_response = nsrApi.request()
        return api_response

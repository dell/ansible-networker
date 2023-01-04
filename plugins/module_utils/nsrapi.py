# Copyright ©️ 2022 Dell Inc. or its subsidiaries.
import requests
import json


class nsrApi:
    def __init__(self, method, url, resource_path, auth, query_params=None, field_params=None, body=None, headers=None):
        self.method = method
        self.query_params = query_params
        self.field_params = field_params
        if headers is None:
            self.headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        else:
            self.headers = headers
        self.body = body
        self.auth = auth
        self.auth = auth
        self.resource_path = resource_path
        field_appender = ''
        query_appender = ''
        self.url = url + resource_path
        if query_params is not None:
            # query_params = eval(query_params)
            if not isinstance(query_params, dict):
                raise TypeError("query_param should be a dictionary type. like {hostname: abc, level: Incr}")
            query_params = " and ".join(str(query_params).split(',')).replace("{", "").replace("}", "").replace("'", '')
            query_appender = 'q=' + query_params
        if field_params is not None:
            # field_params = eval(field_params)
            if not isinstance(field_params, list):
                raise TypeError("query_param should be a list type. like [hostname,level]")
            fields = str(field_params).replace("[", "").replace("]", "").replace(", ", ",").replace("'",  "")
            field_appender = 'fl=' + fields
        if query_params is not None and field_params is not None:
            self.url = self.url + '?' + query_appender + '&' + field_appender
        elif query_params is not None and field_params is None:
            self.url = self.url + '?' + query_appender
        elif query_params is None and field_params is not None:
            self.url = self.url + '?' + field_appender
        else:
            self.url = self.url
        supported_method = ["GET", "HEAD", "OPTIONS", "POST", "PATCH", "PUT", "DELETE"]
        if method not in supported_method:
            raise ValueError(
                "http method must be `GET`, `HEAD`, `OPTIONS`,"
                " `POST`, `PATCH`, `PUT` or `DELETE`."
            )

    def request(self):
        method = self.method
        url = self.url
        query_params = self.query_params
        headers = self.headers
        body = json.dumps(self.body)
        auth = self.auth
        print(url)
        return requests.request(method, url, data=body, auth=auth, headers=headers, verify=False)


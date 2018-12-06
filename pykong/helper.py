#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2018/11/21
@author: shimakaze-git

util functions
'''


import json
import yaml
import sys
import os
import requests

from prettytable import PrettyTable
from requests.exceptions import RequestException


def apis_serializer(data):
    """ apis apis_serializer """

    table = PrettyTable(
        ["key", "value"]
    )
    # table.add_row(["created_at", data['created_at']])
    # table.add_row(["http_if_terminated", data['https_only']])
    table.add_row(["id", data['id']])
    table.add_row(["name", data['name']])
    table.add_row(["preserve_host", data['preserve_host']])
    table.add_row(["retries", data['retries']])
    table.add_row(["strip_uri", data['strip_uri']])
    # table.add_row([
    #     "upstream_connect_timeout",
    #     data['upstream_connect_timeout']
    # ])
    # table.add_row([
    #     "upstream_read_timeout",
    #     data['upstream_read_timeout']
    # ])
    # table.add_row([
    #     "upstream_send_timeout",
    #     data['upstream_send_timeout']
    # ])
    table.add_row(["upstream_url", data['upstream_url']])

    # uris, hosts
    if 'uris' in data:
        table.add_row(["uris", data['uris']])
    if 'hosts' in data:
        table.add_row(["hosts", data['hosts']])

    return table.get_string() + "\n"


def clean_format_params(data, empty_string=False):
    for k in list(data):
        value = data[k]
        if not isinstance(value, (str, int)) or (empty_string and value is ''):
            data.pop(k)
    data.pop('pykong', None)
    return data


def error(message):
    raise RuntimeError(message)


def is_file(path):
    """ is file """
    return os.path.isfile(path)


def pretty_json(obj):
    return json.dumps(obj, sort_keys=True, indent=2 * ' ')


def handle_json_response(response):
    return response.json()
    # if response.ok:
    #     return response.json()
    # else:
    #     print(response.text)


def convertToDict(path):
    """ File convert to dict """

    try:
        if isJsonFormat(path):
            file = open(path, "r")
            data_dict = json.load(file)
        elif isYamlFormat(path):
            file = open(path, "r")
            data_dict = yaml.load(file)
        else:
            raise Exception
        return data_dict
    except Exception as e:
        print('convertToDict')
        print(sys.exc_info())
        print(e)
        sys.exit()


def isYamlFormat(path):
    """ yaml format """
    
    try:
        file = open(path, "r")
        yaml.load(file)
    # except yaml.YAMLError as e:
    #     print(sys.exc_info())
    #     print(e)
    #     print('test')
    #     return False
    except ValueError as e:
        print(sys.exc_info())
        print(e)
        return False
    except Exception as e:
        print(sys.exc_info())
        print(e)
        return False
    return True


def isJsonFormat(path):
    """ json format """
    
    try:
        file = open(path, "r")
        json.load(file)
    # except json.JSONDecodeError as e:
    #     print(sys.exc_info())
    #     print(e)
    #     print('ggegre')
    #     return False
    except ValueError as e:
        print(sys.exc_info())
        print(e)
        return False
    except Exception as e:
        print(sys.exc_info())
        print(e)
        return False
    return True


class RequestHelper(object):
    """ Request Helper Class """

    def __init__(self, request_url):
        self.request_url = request_url
        self.form_header = {
            'Content-type': 'application/x-www-form-urlencoded'
        }

    def get(self, params):
        res = requests.get(
            self.request_url,
            params
        )
        return res

    def post(self, data):
        if self.check_data(data):
            res = requests.post(
                self.request_url,
                data=data,
                headers=self.form_header
            )
            return res
        else:
            print("data is empty")
            sys.exit()

    def put(self, data):
        if self.check_data(data):
            res = requests.put(
                self.request_url,
                data=data,
                headers=self.form_header
            )
            return res
        else:
            print("data is empty")
            sys.exit()

    def patch(self, data):
        if self.check_data(data):
            res = requests.patch(
                self.request_url,
                data=data,
                headers=self.form_header
            )
            return res
        else:
            print("data is empty")
            sys.exit()

    def delete(self):
        res = requests.post(
            self.request_url,
        )
        return res

    def check_data(self, data):
        if data:
            return True
        else:
            return False

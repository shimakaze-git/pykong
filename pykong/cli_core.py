#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2018/11/22
@author: shimakaze-git

command line interface of pykong
'''

import click
from prettytable import PrettyTable

from .core import PyKongCore
from .core import PyKongAPI

from .helper import handle_json_response
from .helper import pretty_json
from .helper import error
from .helper import clean_format_params
from .helper import apis_serializer


class PyKongCLI(object):
    """ PyKong API CLI class"""

    def __init__(self, host, port):
        """ Constructor """
        self.pykong_api = PyKongAPI(host, port)
        self.pykong_plugin = None

    def get_status(self):
        """ get api list """
        res = self.pykong_api.status()
        if res.ok:
            res_json = handle_json_response(res)
            return pretty_json(res_json)
        else:
            error(
                "GET %s Error %s: %s" %
                (res.url, res.status_code, res.text)
            )

    def read_api_list(self, serialize=None):
        """ get api list """
        res = self.pykong_api.get_list()
        if res.ok:
            res_json = handle_json_response(res)
            if serialize is None:
                total = res_json['total']
                api_data = res_json['data']

                table = PrettyTable(
                    ["key", "value"]
                )
                table.add_row(["total", total])
                output_text = table.get_string() + "\n"

                for data in api_data:
                    output_text += apis_serializer(data)
                return output_text
            else:
                return pretty_json(res_json)
        else:
            error(
                "GET %s Error %s: %s" %
                (res.url, res.status_code, res.text)
            )

    def read_api(self, name, serialize=None):
        """ get api """
        res = self.pykong_api.read(name)
        if res.ok:
            res_json = handle_json_response(res)
            if serialize is None:
                return apis_serializer(res_json)
            else:
                return pretty_json(res_json)
        else:
            error(
                "GET %s Error %s: %s" %
                (res.url, res.status_code, res.text)
            )

    def create_api(self, params, serialize=None):
        """ post api """
        params_data = clean_format_params(
            params,
            empty_string=True
        )
        res = self.pykong_api.create(params_data)
        if res.ok:
            res_json = handle_json_response(res)
            if serialize is None:
                return apis_serializer(res_json)
            else:
                return pretty_json(res_json)
        else:
            error(
                "POST %s Error %s: %s" %
                (res.url, res.status_code, res.text)
            )

    def update_api(self, name, params, serialize=None):
        """ update api """
        params_data = clean_format_params(
            params,
            empty_string=False
        )
        res = self.pykong_api.update(params_data)
        if res.ok:
            res_json = handle_json_response(res)
            if serialize is None:
                return apis_serializer(res_json)
            else:
                return pretty_json(res_json)
        else:
            error(
                "PUT %s Error %s: %s" %
                (res.url, res.status_code, res.text)
            )

    def delete_api(self, name, serialize=None):
        """ delete api """
        res = self.pykong_api.delete(name)
        if res.ok:
            return res
            # res_json = handle_json_response(res)
            # if serialize is None:
            #     return apis_serializer(res_json)
            # else:
            #     return pretty_json(res_json)
        else:
            error(
                "DELETE %s Error %s: %s" %
                (res.url, res.status_code, res.text)                
            )

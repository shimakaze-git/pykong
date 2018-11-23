#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2018/11/22
@author: shimakaze-git

command line interface of pykong
'''

import click
from .core import PyKongCore
from .core import PyKongAPI

from .helper import handle_json_response
from .helper import pretty_json
from .helper import error


class PyKongCLI(object):
    """ PyKong CLI class"""

    def __init__(self, host, port):
        self.pykong_api = PyKongAPI(host, port)
        self.pykong_plugin = None

    def get_api_list(self):
        """ get api list """
        res = self.pykong_api.get_list()
        if res.ok:
            res_json = handle_json_response(res)
            return pretty_json(res_json)
        else:
            error(
                "GET %s Error %s: %s" %
                (res.url, res.status_code, res.text)
            )

    def get_api(self, name):
        """ get api """
        res = self.pykong_api.get_api(name)
        if res.ok:
            res_json = handle_json_response(res)
            return pretty_json(res_json)
        else:
            error(
                "GET %s Error %s: %s" %
                (res.url, res.status_code, res.text)
            )
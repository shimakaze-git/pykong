#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2018/11/21
@author: shimakaze-git

core.py is mainthread of pykong.
'''


import os
import sys
import re
import hashlib
import click
import requests
import simplejson as json
import logging
# import ConfigParser

from .helper import convertToDict
from .helper import error
from .helper import RequestHelper
from .helper import handle_json_response


def validate(data):
    """ validation check """
    pass


class PyKongCore(object):
    """ PyKongCore class """

    def __init__(self, host=None, port=None):
        """ Constructor """
        if host:
            self.host = host
        else:
            self.host = "http://127.0.0.1"
        if port:
            self.port = port
        else:
            self.port = 8001

        self.form_header = {
            'Content-type': 'application/x-www-form-urlencoded'
        }

    def echo_req(self):
        pass

    def status(self):
        """ get request status """
        url = self.host + "/status/"
        response = self.get(url)
        return handle_json_response(response)

    def get(self, req_url, params=None):
        try:
            req_helper = RequestHelper(req_url)
            res = req_helper.get(
                params=params
            )
            return res
        except Exception as e:
            print(e)
            error(e)

    def post(self, req_url, data=None):
        try:
            req_helper = RequestHelper(req_url)
            res = RequestHelper.post(
                api_url,
                data=data
            )
            return res
            # error(
            #     "POST %s Error %s: %s" %
            #     (api_url, res.status_code, res.text)
            # )
        except Exception as e:
            print(e)
            error(e)


class PyKongAPI(PyKongCore):
    """ PyKongAPI class"""

    def __init__(self, host, port):
        """ Constructor """
        super(PyKongAPI, self).__init__(host, port)

    def get_api_url(self, path):
        return "%s:%s%s" % (self.host, self.port, path)

    def create(self, data=''):
        """ create api """
        url = self.get_api_url('/apis/')
        response = self.post(url, data)
        return response

    def get_list(self):
        """ get api list """
        url = self.get_api_url('/apis/')
        response = self.get(url)
        return response

    def get_api(self, name):
        """ get api """
        url = self.get_api_url('/apis/%s' % name)
        response = self.get(url)
        return response

    def add_list(self, api_list: dict):

        # validation check
        # validate(json_dict)

        for name in api_list:
            api_info = api_list[name]
            upstream_url = api_info['upstream_url']
            uris = api_info['uris']
            print(api_info)
            
            # api_url = self.get_api_url("/apis/")
            
            res = self.create()
            # r = requests.post(url, json=json)
            # print(api_url)

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
import time
# import requests
import simplejson as json
import logging
# import ConfigParser

from .helper import convertToDict
from .helper import error
from .helper import RequestHelper
# from .helper import handle_json_response
from .helper import RequestException

from retry import retry
from random import randint

MAX_RETRY = 5


def validate(data):
    """ validation check """
    pass


def echo_req(request_func):
    """ echo request decorator """

    def echo_request_check(req_url):
        try:
            # req_url = 'http://127.0.0.1:7000'
            req_helper = RequestHelper(req_url)
            res = req_helper.get(params=None)
        except RequestException as e:
            sys.stderr.write(
                'Failed to connect to Kong (%s)'
                % (req_url)
            )
            # print(e)
            sys.exit()

    def exponential_backoff(*args, **kwargs):
        # exponential backoff

        result = None
        retry_counter = 0
        for i in range(MAX_RETRY):
            try:
                result = request_func(*args, **kwargs)
                break
            except Exception as e:
                retry_counter += 1
                sleep_time = randint(
                    0, 2**retry_counter
                )
                # print(e)
                print("retry after %s second" % (sleep_time))
                time.sleep(sleep_time)
                continue
        return result

    def echo_kong(*args, **kwargs):
        """ echo request to kong """

        core_obj = args[0]
        req_url = core_obj.admin_url

        # echo request to kong
        echo_request_check(req_url)

        result = exponential_backoff(*args, **kwargs,)

        if result:
            return result
        else:
            sys.stderr.write(
                'Request connection to timeout'
            )
            sys.exit()
    return echo_kong


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
        self.admin_url = self.host + ":" + str(self.port)

        self.form_header = {
            'Content-type': 'application/x-www-form-urlencoded'
        }

    def status(self):
        """ get request status """
        url = self.admin_url + "/status/"
        response = self.get(url)
        return response

    @echo_req
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

    @echo_req
    def post(self, req_url, data=None):
        try:
            req_helper = RequestHelper(req_url)
            res = req_helper.post(
                data=data
            )
            return res
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

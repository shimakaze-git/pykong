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

# from .helper import convertToDict
from .helper import RequestHelper
from .helper import error



def validate(data):
    """ validation check """
    pass


class PyKongCore(object):

    def __init__(self, host):
        
        if host:
            self.host = host
        else:
            self.host = "http://127.0.0.1:8001"
            
        self.form_header = {
            'Content-type': 'application/x-www-form-urlencoded'
        }

    def echo_req(self):
        pass

    def get_api_url(self, path):
        return "%s%s" % (self.host, path)

    def create(self, data=''):
        """ create api """

        try:
            api_url = self.get_api_url("/apis/")
            res = RequestHelper.post(
                api_url,
                data=data
            )

            if res.ok:
                return res
            else:
                error(
                    "POST %s Error %s: %s" % \
                    (api_url, res.status_code, res.text)
                    # "POST %s with data: %s, Error %s: %s" % \
                    # (url, pretty_json(data), res.status_code, r.text)
                )
        except Exception as e:
            print(e)
            error(e)

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



@click.group()
# @click.option('--conf', envvar='KONG_CONF', default=os.path.expanduser("~/.kong"))
# @click.option('--debug/--no-debug', envvar='KONG_DEBUG', default=False)
# @click.pass_context
def cli(ctx, conf, debug):
    # ctx.obj = Kong(conf, debug)
    print(ctx, conf, debug)



if __name__ == '__main__':
    pass
    # path = "../tests/test.json"
    # path = "../tests/test.yml"
    # pykong_obj = PyKongCore()
    # pykong_obj.add_list(path)
    # pykong_obj
    # print(pykong_obj)
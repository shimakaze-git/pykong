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


def error(message):
    raise RuntimeError(message)


def is_file(path):
    """ is file """

    return os.path.isfile(path)

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
            raise
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
    
    def __init__(self, request_url):
        self.request_url = request_url
        self.form_header = {
            'Content-type': 'application/x-www-form-urlencoded'
        }

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

    def check_data(self, data):
        if data:
            return True
        else:
            return False
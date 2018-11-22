#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2018/11/21
@author: shimakaze-git

pykong-cli.py is cli of pykong
'''
import re
import sys
import os

path = os.path.join(os.path.dirname(__file__), '../')
sys.path.append(path)
from pykong import cli


if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-bin\.pyw?|\.exe)?$', '', sys.argv[0])
    # print(sys.argv)
    sys.exit(cli())
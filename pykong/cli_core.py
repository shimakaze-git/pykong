#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2018/11/22
@author: shimakaze-git

command line interface of pykong
'''

import click
from .core import PyKongCore
from .helper import convertToDict
from .helper import is_file


# @click.group()
# # @click.option('--conf', envvar='KONG_CONF', default=os.path.expanduser("~/.kong"))
# # @click.option('--debug/--no-debug', envvar='KONG_DEBUG', default=False)
# # @click.pass_context
# def cli(ctx, conf, debug):
#     # ctx.obj = Kong(conf, debug)
#     print(ctx, conf, debug)


# @click.group()
# # @click.option('--conf', envvar='KONG_CONF', default=os.path.expanduser("~/.kong"))
# # @click.option('--debug/--no-debug', envvar='KONG_DEBUG', default=False)
# # @click.pass_context
# def cli(ctx, conf, debug):
#     # ctx.obj = Kong(conf, debug)
#     print(ctx, conf, debug)

@click.group(help="pykong config")
@click.option('--host', '-h', default='127.0.0.1:8001', help='kong hosturl and port.')
# @click.argument('name')
@click.pass_context
def cli(ctx, host):
    ctx.obj = PyKongCore(host=host)


@cli.command()
@click.pass_obj
def english(pykong):
    print(pykong)
    click.echo('Hello, World!')


@cli.command()
@click.option('--test', '-t', type=str, default='test', help='test.')
@click.pass_obj
def japanese(pykong):
    pass
    # click.echo('Konnichiwa, Sekai!, {test} !'.format(test=test))



def validate_isfile(file):
    """ validation check """

    if not is_file(file):
        raise click.BadParameter('List File Does Not Exist.')

@cli.command()
@click.option('--file', '-f', type=str, help='test.')
@click.pass_obj
def add(pykong, file):
    
    validate_isfile(file)
    api_list = convertToDict(file)
    print(api_list)
    # print(pykong)
    # print(vars())

# https://blog.amedama.jp/entry/2015/10/14/232045
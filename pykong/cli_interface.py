#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2018/11/22
@author: shimakaze-git

command line interface of pykong
'''

import click
from .core import PyKongCore
from .cli_core import PyKongCLI
from .helper import convertToDict
from .helper import is_file


# @click.group()
# # @click.option('--conf', envvar='KONG_CONF', default=os.path.expanduser("~/.kong"))
# # @click.option('--debug/--no-debug', envvar='KONG_DEBUG', default=False)
# # @click.pass_context
# def cli(ctx, conf, debug):
#     # ctx.obj = Kong(conf, debug)
#     print(ctx, conf, debug)

def validate_port(ctx, param, port):
    """ validation check port"""

    if port > 65535:
        raise click.BadParameter('The Numeric of port is out of range.')


def validate_isfile(file):
    """ validation check """

    if not is_file(file):
        raise click.BadParameter('List File Does Not Exist.')


@click.group(help="pykong config")
@click.option('--host', '-h', default='http://127.0.0.1', help='kong hosturl.')
@click.option('--port', '-p', type=int, callback=validate_port, default='8001', help='kong port.')
# @click.argument('name')
@click.pass_context
def cli(ctx, host, port):
    ctx.obj = PyKongCLI(host=host, port=port)
    # pass


@cli.command("add")
@click.option('--file', '-f', type=str, help='test.')
@click.pass_obj
def add(pykong, file):
    validate_isfile(file)
    api_list = convertToDict(file)
    print(api_list)
    # print(pykong)
    # print(vars())


# @cli.group()
@cli.command("status")
@click.pass_obj
def status(pykong):
    click.echo(pykong.get_status())


@cli.group()
@click.pass_obj
def api(pykong):
    pass


@api.command("list")
@click.pass_obj
def api_list(pykong):
    click.echo(pykong.get_api_list())

# https://blog.amedama.jp/entry/2015/10/14/232045

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
@click.option(
    '--port',
    '-p',
    type=int,
    callback=validate_port,
    default='8001',
    help='kong port.'
)
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





""""""" API """""""

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
@click.option(
    '--serialize',
    '-s',
    help="serialize response format",
    type=click.Choice(['default', 'json'])
)
@click.pass_obj
def api_list(pykong, serialize):
    click.echo(pykong.read_api_list(
        serialize=serialize
    ))


@api.command("get")
@click.option(
    '--name', '-n', prompt='name',
    type=str, help='api name'
)
@click.option(
    '--serialize',
    '-s',
    help="serialize response format",
    type=click.Choice(['default', 'json'])
)
@click.pass_obj
def api_get(pykong, name, serialize):
    click.echo(pykong.read_api(
        name=name,
        serialize=serialize
    ))


@api.command("add")
@click.option(
    '--name', '-n', prompt='name',
    type=str, help='api name'
)
@click.option(
    '--upstream-url', '-u', prompt='upstream url',
    type=str, help="The base target URL that points to your API server."
)
@click.option(
    '--uris', prompt="uris",
    type=str, help="list of URIs prefixes that point to your API."
)
# @click.option('--hosts', prompt='hosts', default="example.com", help="A comma-separated list of domain names that point to your API")
# @click.option('--uris', prompt='uris', default="", help="A comma-separated list of URIs prefixes that point to your API.")
# @click.option('--methods', prompt='methods', default="GET,PUT,POST,DELETE", help="A comma-separated list of HTTP methods that point to your API.")
# @click.option('--upstream-url', prompt='upstream url', default="https://example.com", help="The base target URL that points to your API server. ")
# @click.option('--strip-uri', help="When matching an API via one of the uris prefixes, strip that matching prefix from the upstream URI to be requested. ")
# @click.option('--preserve-host', help="When matching an API via one of the hosts domain names, make sure the request Host header is forwarded to the upstream service.")
# @click.option('--retries', help="The number of retries to execute upon failure to proxy. ")
# @click.option('--upstream-connect-timeout', help="The timeout in milliseconds for establishing a connection to your upstream service. ")
# @click.option('--upstream-send-timeout', help="The timeout in milliseconds between two successive write operations for transmitting a request to your upstream service")
# @click.option('--upstream-read-timeout', help="The timeout in milliseconds between two successive read operations for transmitting a request to your upstream service")
@click.option('--https-only', help="")
# @click.option('--http-if-terminated', help="Consider the X-Forwarded-Proto header when enforcing HTTPS only traffic")
@click.option(
    '--serialize',
    '-s',
    help="serialize response format",
    type=click.Choice(['default', 'json'])
)
@click.pass_obj
def api_add(
    pykong,
    name,
    upstream_url,
    uris,
    https_only,
    serialize
):
    click.echo(
        pykong.create_api(
            params=vars(),
            serialize=serialize
        )
    )


@api.command("update")
@click.option(
    '--name', '-n', prompt='name',
    type=str, help='api name'
)
@click.option(
    '--upstream-url', '-u', prompt='upstream url',
    type=str, help="The base target URL that points to your API server."
)
@click.option(
    '--uris', prompt="uris",
    type=str, help="list of URIs prefixes that point to your API."
)
@click.option('--https-only', help="")
@click.option(
    '--serialize',
    '-s',
    help="serialize response format",
    type=click.Choice(['default', 'json'])
)
@click.pass_obj
def api_update(
    pykong,
    name,
    upstream_url,
    uris,
    https_only,
    serialize
):
    params = vars()
    params.pop("name")

    click.echo(
        pykong.update_api(
            name=name,
            params=params,
            serialize=serialize
        )
    )


@api.command("delete")
@click.option(
    '--name', '-n', prompt='name',
    type=str, help='api name'
)
@click.option(
    '--serialize',
    '-s',
    help="serialize response format",
    type=click.Choice(['default', 'json'])
)
@click.pass_obj
def api_delete(
    pykong,
    name,
    serialize
):
    click.echo(
        pykong.delete_api(
            name=name,
            serialize=serialize
        )
    )


""""""" Consumers """""""



""""""" Pluguin """""""
# -*- coding: utf-8 -*-
"""
    emdata_clean.cli
    ~~~~~~~~~

"""

import click


class Config(object):
    """docstring for Config."""

    def __init__(self, arg):
        super(Config, self).__init__()
        self.verbose = False

pass_config = click.make_pass_decorator(Config)


@click.group()
@click.option('--verbose', is_flag=True)
def cli(verbose):
    if verbose:
        print('We are in verbose mode')


@cli.command('delete', short_help='Runs a datas delete.')
@click.option('--string', default='World',
              help='This the thing that is greeted.')
@click.option('--repeat', default=1,
              help='How many times you should be greeted.')
@click.argument('out', type=click.File('w'), default='-',
                required=False)
def delete(string, repeat):
    for x in range(repeat):
        print('Hello %s!' % string, file=out)

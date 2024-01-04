from argparse import ArgumentParser

from redstat.redload.cli.arguments.optional import register_type_parser
from redstat.redload.cli.arguments.positional import register_name_argument
from redstat.redload.variables.url_types import USER_URL_TYPES


def register_user_parser(subparser, parents: list[ArgumentParser]):
    user_parents = parents.copy()
    user_parents.extend([
        register_name_argument('reddit username'),
        register_type_parser(USER_URL_TYPES),
    ])

    user_parser: ArgumentParser = subparser.add_parser('user', help='user parser', parents=user_parents)

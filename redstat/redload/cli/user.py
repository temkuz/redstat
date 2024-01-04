from argparse import ArgumentParser

from redstat.redload.cli.arguments.optional import register_type_parser
from redstat.redload.cli.arguments.positional import register_name_argument
from redstat.redload.functions import download_statistic
from redstat.redload.variables.url_types import USER_URL_TYPES
from redstat.shared_resources.cli.arguments import optional as shared_optional
from redstat.shared_resources.cli.defaults import register_default_func


def register_user_parser(subparser):
    parents = [
        register_name_argument('reddit username'),
        register_default_func(download_statistic),
        register_type_parser(USER_URL_TYPES),
        shared_optional.register_output_argument()
    ]

    default_parser: ArgumentParser = subparser.add_parser('user', help='user parser', parents=parents)

from argparse import ArgumentParser

from redstat.redload.cli.arguments.optional import register_type_parser
from redstat.redload.cli.arguments.positional import register_name_argument
from redstat.redload.functions import download_statistic
from redstat.redload.variables.url_types import SUBREDDIT_URL_TYPES
from redstat.shared_resources.cli.arguments.optional import register_output_argument
from redstat.shared_resources.cli.defaults import register_default_func


def register_post_parser(subparser):
    parents = [
        register_name_argument('subreddit name'),
        register_default_func(download_statistic),
        register_type_parser(SUBREDDIT_URL_TYPES),
        register_output_argument()
    ]
    default_parser: ArgumentParser = subparser.add_parser('subreddit', help='subreddit parser', parents=parents)

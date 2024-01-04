from argparse import ArgumentParser

from redstat.redload.cli.arguments.optional import register_type_parser
from redstat.redload.cli.arguments.positional import register_name_argument
from redstat.redload.variables.url_types import SUBREDDIT_URL_TYPES


def register_subreddit_parser(subparser, parents: list[ArgumentParser]):
    subreddit_parents = parents.copy()
    subreddit_parents.extend([
        register_name_argument('subreddit name'),
        register_type_parser(SUBREDDIT_URL_TYPES)
    ])
    subreddit_parser: ArgumentParser = subparser.add_parser('subreddit', help='subreddit parser',
                                                            parents=subreddit_parents)

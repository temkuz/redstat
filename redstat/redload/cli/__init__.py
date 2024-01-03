from argparse import ArgumentParser
from sys import argv

from redstat.redload.cli.subreddit import register_post_parser
from redstat.redload.cli.user import register_user_parser

from redstat.redload.variables.cli import CLI_DESCRIPTION


def parse_args():
    default_parser = ArgumentParser(description=CLI_DESCRIPTION)
    subparser = default_parser.add_subparsers()

    register_subparsers(subparser)

    if len(argv) == 1:
        default_parser.print_help()
        exit()

    return default_parser.parse_args()


def register_subparsers(subparser):
    register_post_parser(subparser)
    register_user_parser(subparser)

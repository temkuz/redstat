from argparse import ArgumentParser
from sys import argv

from redstat.redload.cli.arguments.optional import register_type_parser
from redstat.redload.cli.arguments.positional import register_name_argument
from redstat.redload.cli.subreddit import register_subreddit_parser
from redstat.redload.cli.user import register_user_parser
from redstat.redload.functions import download_statistic
from redstat.redload.variables.cli import CLI_DESCRIPTION

from redstat.shared_resources.cli.arguments.optional.verbose import register_verbose_argument
from redstat.shared_resources.cli.arguments.optional.output import register_output_file_argument, \
    register_output_dir_argument

from redstat.shared_resources.cli.defaults import register_default_func


def parse_args():
    root_parents = [
        register_verbose_argument(),
        register_default_func(download_statistic),
        register_output_file_argument(),
        register_output_dir_argument(),
    ]
    default_parser = ArgumentParser(description=CLI_DESCRIPTION, parents=root_parents)
    subparser = default_parser.add_subparsers(required=True)

    register_subparsers(subparser, root_parents)

    return default_parser.parse_args()


def register_subparsers(subparser, root_parents):
    register_subreddit_parser(subparser, root_parents)
    register_user_parser(subparser, root_parents)

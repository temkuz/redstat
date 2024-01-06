from argparse import ArgumentParser


from redstat.redload.cli.arguments.positional import register_name_argument
from redstat.redload.functions import download
from redstat.redload.variables.cli import CLI_DESCRIPTION

from redstat.shared_resources.cli.arguments.optional.verbose import register_verbose_argument
from redstat.shared_resources.cli.arguments.optional.output import register_output_file_argument

from redstat.shared_resources.cli.defaults import register_func_default


def parse_args():
    root_parents = [
        register_name_argument(),
        register_func_default(download),
        register_output_file_argument(),
        register_verbose_argument()
    ]
    default_parser = ArgumentParser(description=CLI_DESCRIPTION, parents=root_parents)
    return default_parser.parse_args()


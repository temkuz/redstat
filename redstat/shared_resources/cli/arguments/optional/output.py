from argparse import ArgumentParser

from redstat.shared_resources.cli.arguments.types import output_file_type, output_dir_type


def register_output_file_argument():
    parser = ArgumentParser(add_help=False)
    parser.add_argument('-of', '--output-file', help='output file', type=output_file_type)
    return parser


def register_output_dir_argument():
    parser = ArgumentParser(add_help=False)
    parser.add_argument('-od', '--output-dir', help='output dir', type=output_dir_type)
    return parser

from argparse import ArgumentParser

from redstat.redload.functions import download_statistic


def register_function_default() -> ArgumentParser:
    default_parser = ArgumentParser(add_help=False)
    default_parser.set_defaults(func=download_statistic)
    return default_parser

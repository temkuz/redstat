from argparse import ArgumentParser


def register_default_func(func):
    default_parser = ArgumentParser(add_help=False)
    default_parser.set_defaults(func=func)
    return default_parser

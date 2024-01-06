from redstat.redload.cli import parse_args

from .functions.validate import validate


def main():
    namespace = parse_args()
    validate(namespace)

    if namespace.verbose:
        print(namespace)

    namespace.func(namespace)

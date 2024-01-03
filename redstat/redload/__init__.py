from redstat.redload.cli import parse_args


def main():
    namespace = parse_args()

    if namespace.func is None:
        raise Exception(f'Invalid input {namespace}')

    namespace.func(namespace)

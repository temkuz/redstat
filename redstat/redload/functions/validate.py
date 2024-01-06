def validate(namespace):
    validate_func(namespace)
    validate_name(namespace.name)


def validate_name(name: str) -> None:
    name_prefix = ('r/', 'u/')
    if not name.startswith(name_prefix):
        raise ValueError(f"Resource must start with: {', '.join(f'{prefix!r}' for prefix in name_prefix)}")


def validate_func(namespace):
    if namespace.func is None:
        raise AttributeError(f'Invalid input {namespace}. Func not set')

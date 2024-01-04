from typing import TextIO


def format_file(namespace) -> TextIO:
    if namespace.output_file is None:
        json_name = open(f'{namespace.name}.json', 'w', encoding='utf-8')
    else:
        json_name = namespace.output_file

    return json_name


def format_url(data: dict, type_: str, name: str):
    return data[type_].format(name)

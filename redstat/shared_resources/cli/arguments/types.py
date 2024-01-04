from argparse import FileType
from pathlib import Path

output_file_type = FileType('w', encoding='utf-8')


def output_dir_type(folder_name=None) -> Path | None:
    if folder_name is None:
        return folder_name
    folder = Path(folder_name)
    folder.mkdir(parents=True, exist_ok=True)
    return folder

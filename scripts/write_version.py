import sys

import toml

from pathlib import Path
from tricky.iterables import filter_item


def write_stdout(*text: str):
    text += ('\n',)
    sys.stdout.write(''.join(text))


def get_project_version() -> None:
    parent_dir: Path = Path('./').absolute()
    pyproject_path: Path = parent_dir / 'pyproject.toml'

    with open(pyproject_path, 'r') as file:
        project_info: dict = toml.load(file)
        version: str = project_info['tool']['poetry']['version']
    init_file_path: Path = parent_dir / 'tricky' / '__init__.py'
    with open(init_file_path, 'r') as file:
        lines = file.readlines()
        current_version_line: str = filter_item(
            lines,
            lambda line: '__version__' in line,
            version,
        )
        current_version: str = current_version_line.strip("__version__ = ")
        write_stdout(f'Current version: \'{version}\'')

    if version in current_version:
        write_stdout('No version updates detected.')
    else:
        write_stdout(f'Updated current version to: \'{version}\'')
    file_data = ''.join(lines).replace(current_version_line, f'__version__ = \'{version}\'\n')
    with open(init_file_path, 'w') as file:
        file.write(file_data)

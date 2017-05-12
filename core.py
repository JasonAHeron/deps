import os
from pathlib import Path
from collections import namedtuple

Directory = namedtuple('Directory', ['owners', 'dependencies'])

OWNERS = '/OWNERS'
DEPENDENCIES = '/DEPENDENCIES'
DEBUG = True

def check_directory(directory):
    if DEBUG:
        print('checking {}'.format(directory))
    owners_file = Path(directory + OWNERS)
    dependency_file = Path(directory + DEPENDENCIES)
    owners_data = read_file(owners_file) if owners_file.exists() else None
    dependency_data = read_file(dependency_file) if dependency_file.exists() else None
    return Directory(owners=owners_data, dependencies=dependency_data)


def read_file(file_path):
    with open(file_path, 'r') as data:
        return [line.strip() for line in data.readlines()]

def main():
    ROOT = os.getcwd() + '/src'
    print(check_directory(ROOT))
    print(check_directory(ROOT + '/backend'))

main()
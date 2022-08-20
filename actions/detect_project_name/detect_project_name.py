#!/usr/bin/env python3

import argparse
import configparser
import pathlib
import sys


def run(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('project', type=pathlib.Path,
                        help='Path to the defold project.')
    parser.add_argument('--append-to', type=pathlib.Path,
                        help='Path to the env file.')
    args = parser.parse_args(argv)

    project_file = args.project / 'game.project'
    config = configparser.ConfigParser()
    config.read(project_file, encoding='utf-8')
    project_name = config.get('project', 'title')

    print(f'::set-output name=project_name={project_name}')

    if args.append_to is not None:
        with args.append_to.open('a', encoding='utf-8') as f:
            f.write(f'DEFOLD_PROJECT_NAME={project_name}\n')

if __name__ == '__main__':
    sys.exit(run())

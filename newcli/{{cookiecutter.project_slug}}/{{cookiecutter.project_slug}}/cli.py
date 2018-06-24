import sys
import click
from {{cookiecutter.project_slug}}.core import {{cookiecutter.project_slug}}

@click.group()
def cli():
    """{{cookiecutter.project_slug}}
    """
    if sys.version_info[0] == 2:
        print("Current environment is Python 2.")
        print("Please use a Python 3 virtualenv")
        raise SystemExit


def main():
    cli()


if __name__ == '__main__':
    main()

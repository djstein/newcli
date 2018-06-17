import sys
import click
from newcli.core import new_project

@click.group()
def cli():
    """newcli
    """
    if sys.version_info[0] == 2:
        print("Current environment is Python 2.")
        print("Please use a Python 3 virtualenv")
        raise SystemExit


@cli.command()
def init():
    """Create new project."""
    new_project()


def main():
    cli()


if __name__ == '__main__':
    main()

import sys
import click
from bigcheese.core import bigcheese

@click.group()
def cli():
    """bigcheese
    """
    if sys.version_info[0] == 2:
        print("Current environment is Python 2.")
        print("Please use a Python 3 virtualenv")
        raise SystemExit


def main():
    cli()


if __name__ == '__main__':
    main()

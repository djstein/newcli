import click
from newcli.management import new_project

@click.group()
def cli():
    """newcli
    """
    if sys.version_info[0] == 2:
        print("Current environment is Python 2.")
        print("Please use a Python 3 virtualenv")
        raise SystemExit


@cli.command('init')
def new_project():
    """Create new project."""
    new_project()


def main():
    cli()


if __name__ == '__main__':
    main()

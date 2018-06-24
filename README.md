# newcli

Utility to create a new Python CLI.

## Quickstart

```python
pipenv install newcli
newcli init
```

## Install

```python
# Command(s)

pipenv install newcli
pip3 install --user newcli
```

## Commands

### `init`

```python
# Command

newcli init
```

`newci` will then prompt you for basic information about your project!
The output creates this folder structure:

```bash
{{project}}/
├── LICENSE
├── MANIFEST.in
├── Pipfile
├── README.md
├── setup.py
├── tox.ini
└── {{project}}
    ├── __init__.py
    ├── __version__.py
    ├── cli.py
    └── core.py
```

## TODO

-   100% unit tests and run on TravisCI
-   populate GitHub information from .gitconfig
-   add .travis.yml configuration
-   add template tox configuration
-   add template test files and folder structure
-   add template README.md

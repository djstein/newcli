import os
import shutil
from subprocess import call
from cookiecutter.main import cookiecutter

ROOT_DIR = os.path.dirname(__file__)
PROJECT_TEMPLATE_DIR = os.path.join(ROOT_DIR, 'templates', '{{project}}')

# def copy_template(source_dir, dest_dir):
    # shutil.copytree(source_dir, dest_dir)

def setup_new_project(dest_dir=os.getcwd()):
    # dest_dir = os.path.join(dest_dir, config.get('{{project}}'))
    # copy_template(PROJECT_TEMPLATE_DIR, dest_dir)

    cookiecutter(ROOT_DIR)
    create_github_repo(config)

def create_github_repo(config, push=True):
    '''If in new project directory, begin clone and push to GitHub.'''
    pass
    # path = '.'
    # call(["git", "init", path])
    # call(["git", "-C", path, "add", "."])
    # call(["git", "-C", path, "commit", "-m", "'Initial Commit - from newcli'"])
    # call(["git", "-C", path, "remote", "add", "origin", repository])
    # if push:
    #     call(["git", "-C", path, "push", "-u", "origin", "master"])

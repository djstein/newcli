import os
from findreplace.core import findreplace

ROOT_DIR = os.path.dirname(__file__)
PROJECT_TEMPLATE_DIR = os.path.join(ROOT_DIR, 'templates', '{{project}}')

def copy_template(source_dir, dest_dir):
    shutil.copytree(source_dir, dest_dir)

def setup_new_project(dest_dir=os.getcwd()):
    config = prompt_config()
    copy_template(ROOT_DIR, dest_dir)
    findreplace(base_dir=dest_dir, find_replace_dict=config)

def prompt_config():
    config = {}
    config['project'] = input("Project Name: ")
    config['name'] = input("Name: ")
    config['github_user'] = input("GitHub Username: ")
    config['github_repo'] = input("GitHub Repository: [https://github.com/{}/{}]".format(config['github_user'], config['project']))
    config['description'] = input("Description: ")
    return config

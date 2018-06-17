
def new_project():
    config = prompt_config()

def prompt_config():
    config = {}
    config['project'] = input("Project Name: ")
    config['name'] = input("Name: ")
    config['github_user'] = input("GitHub Username: ")
    config['github_repo'] = input("GitHub Repository: [https://github.com/{}/{}]".format(config['github_user'], config['project']))
    config['description'] = input("Description: ")
    return config

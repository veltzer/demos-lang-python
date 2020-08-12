from github import Github
import sys
import os.path

sys.path.insert(0,os.path.expanduser("~/.config/pydmt"))
import user.passwords

# connect using username and password
g = Github(user.passwords.github_username, user.passwords.github_password)

# list all projects
for repo in g.get_user().get_repos():
        print(repo.name)
        print("\t"+repo.description)
        print("\t"+repo.html_url)
        if repo.homepage:
            print("\t"+repo.homepage)
        # print("\t"+"\n".join(dir(repo)))
        # sys.exit(1)

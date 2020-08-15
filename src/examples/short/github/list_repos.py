from github import Github

import pyapikey
token = pyapikey.get_key("github")
g = Github(login_or_token=token)

for repo in g.get_user().get_repos():
    print(repo.name)
    if repo.description:
        print(f"\t{repo.description}")
    if repo.html_url:
        print(f"\t{repo.html_url}")
    if repo.homepage:
        print(f"\t{repo.homepage}")

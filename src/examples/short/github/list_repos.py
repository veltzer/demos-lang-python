import sys
import json
import github
import pyapikey

token = pyapikey.get_key("github")
g = github.Github(login_or_token=token)

for repo in g.get_user(login="veltzer").get_repos():
    print(dir(repo))
    # this is json data that descrbies the entire repo
    print(repo.raw_data)
    json.dump(obj=repo.raw_data, fp=sys.stdout, indent=4, sort_keys=True)
    print(repo.name)
    if repo.description:
        print(f"\t{repo.description}")
    if repo.html_url:
        print(f"\t{repo.html_url}")
    if repo.homepage:
        print(f"\t{repo.homepage}")

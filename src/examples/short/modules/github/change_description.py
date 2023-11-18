import github
import pyapikey

token = pyapikey.get_key("github")
g = github.Github(login_or_token=token)

repo = g.get_repo("veltzer/ask")

new_description = "This is the new description for the repository."
repo.edit(description=new_description)

"""
This is an example of how to list google profiles in the current unix account.
"""


import os.path
import json


def main():
    path = os.path.expanduser("~/.config/google-chrome/Local State")
    with open(path) as file_handle:
        data = json.load(file_handle)
    # print(data["profile"]["info_cache"].keys())
    profiles = {}
    for k, v in data["profile"]["info_cache"].items():
        v["profile"] = k
        profiles[v["name"]] = v
    print(profiles)


if __name__ == "__main__":
    main()

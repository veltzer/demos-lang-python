"""
This example shows how to use the openshift API for listing all pods
"""


import subprocess

import openshift.dynamic


def get_project():
    return subprocess.check_output([
        "oc",
        "project",
        "-q",
    ]).decode().rstrip()


def main():
    # you can use "default" in the next line
    # with openshift.project("kube-system"):
    client = openshift.dynamic.client.DynamicClient(client="default")
    pods = client.resources.get(api_version="v1", kind="Pod").get()
    for pod in pods.items:
        print(pod.metadata.name)


if __name__ == "__main__":
    main()

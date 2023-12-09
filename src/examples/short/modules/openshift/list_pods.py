"""
This example shows how to use the openshift API for listing all pods
"""


import subprocess
import openshift


def get_project():
    project = subprocess.check_output([
        "oc",
        "project",
        "-q",
    ]).decode().rstrip()
    return project


def main():
    # you can use "default" in the next line
    with openshift.project("kube-system"):
        for pod_obj in openshift.selector('pods').objects():
            name = pod_obj.name()
            print(name)


if __name__ == "__main__":
    main()

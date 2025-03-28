"""
Reads the list of available API versions and prints them. Similar to running
`kubectl api-versions`.
"""

import kubernetes.client
import kubernetes.config


def main():
    # Configs can be set in Configuration class directly or using helper
    # utility. If no argument provided, the config will be loaded from
    # default location.
    kubernetes.config.load_kube_config()

    print("Supported APIs (* is preferred version):")
    versions = ",".join(kubernetes.client.CoreApi().get_api_versions().versions)
    core = "core"
    print(f"{core:<40} {versions}")
    for api in kubernetes.client.ApisApi().get_api_versions().groups:
        versions = []
        for v in api.versions:
            name = ""
            if v.version == api.preferred_version.version and len(
                    api.versions) > 1:
                name += "*"
            name += v.version
            versions.append(name)
        versions_str = ",".join(versions)
        print(f"{api.name:<40} {versions_str}")


if __name__ == "__main__":
    main()

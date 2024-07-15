"""
A basic demos of listing all pods in k8s

References:
- https://github.com/kubernetes-client/python
"""

import kubernetes.config
import kubernetes.client


def main():
    # Configs can be set in Configuration class directly or using helper utility
    # You have to read the config in order to know the address and credentials
    # by which to contact the cluster
    kubernetes.config.load_config()

    v1 = kubernetes.client.CoreV1Api()
    print("Listing pods with their IPs:")
    #ret = v1.list_pod_for_all_namespaces(watch=False)
    ret = v1.list_namespaced_pod("default")
    for i in ret.items:
        assert i.status is not None
        assert i.metadata is not None
        print(f"{i.status.pod_ip} {i.metadata.namespace} {i.metadata.name}")


if __name__ == "__main__":
    main()

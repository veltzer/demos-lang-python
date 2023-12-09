"""
This example shows how to register on namespace events and wakeup every time
something interesting happens in that namespace with the details

References:
- https://github.com/kubernetes-client/python
"""

import kubernetes.client
import kubernetes.watch
import kubernetes.config


def main():
    # Configs can be set in Configuration class directly or using helper utility
    kubernetes.config.load_config()

    v1 = kubernetes.client.CoreV1Api()
    count = 10
    w = kubernetes.watch.Watch()
    for event in w.stream(v1.list_namespace, _request_timeout=60):
        f_type = event["type"]
        f_object = event["object"]
        print(f"Event: {f_type} {f_object.metadata.name}")
        count -= 1
        if not count:
            w.stop()

    print("Ended.")


if __name__ == "__main__":
    main()

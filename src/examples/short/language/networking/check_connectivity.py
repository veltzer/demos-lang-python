""" check_connectivity.py """

import socket
import time


def measure_response_time(host="8.8.8.8", port=53, timeout=0.05):
    """
    Check your connectivity to the internet by trying to connect to 8.8.8.8
    at port 53 (DNS).
    Args:
    host: The hostname or IP address to connect to.
    port: The port number to connect on (default: 80 for HTTP).
    timeout: The maximum time (seconds) to wait for a connection.
    Returns:
        The time taken to establish a connection in seconds, or None if theres an error.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            start_time = time.time()
            sock.connect((host, port))
            end_time = time.time()
            return end_time - start_time
    except socket.error as err:
        print(f"Error connecting to {host}:{port}: {err}")
        return None


connection_time = measure_response_time()

if connection_time:
    print(f"Connection establishment time to {connection_time:.6f} seconds")
else:
    print("Not connected")

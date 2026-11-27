"""
This is an example of how to use the "dispy" distribution
cluster
"""


import random
import socket
import time

import dispy


def compute(n: int):
    """ "compute" is distributed to each node running "dispynode" """
    time.sleep(n)
    host = socket.gethostname()
    return host, n


def main() -> None:
    cluster = dispy.JobCluster(compute)
    jobs = []
    for i in range(10):
        # schedule execution of "compute" on a node (running "dispynode")
        # with a parameter (random number in this case)
        job: dispy.DispyJob = cluster.submit(random.randint(5, 20))
        job.id = i  # optionally associate an ID to job (if needed later)
        jobs.append(job)
    # cluster.wait() # waits for all scheduled jobs to finish  # noqa: ERA001  teaching: kept in the comment for the reader
    for job in jobs:
        host, n = job()  # waits for job to finish and returns results
        print(f"{host} executed job {job.id} at {job.start_time} with {n}")
        # other fields of "job" that may be useful:
        # print(job.stdout, job.stderr, job.exception, job.ip_addr, job.start_time, job.end_time)  # noqa: ERA001  teaching: kept in the comment for the reader
    cluster.print_status()


if __name__ == "__main__":
    main()

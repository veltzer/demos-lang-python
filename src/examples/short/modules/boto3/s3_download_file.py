"""
This is an example of how to download a single file from s3
This is how to download the file to a local file, not to RAM.

References:
- https://www.radishlogic.com/aws/s3/how-to-download-files-from-s3-bucket-using-boto3-and-python/
"""

import boto3

bucket_name = "litebc-upload"
key = "10k/2023-05-02/18934974-d25a-4895-8208-b707ee2d586c_0/0/recording_id.txt"
local = "/tmp/recording_id.txt"

s3 = boto3.resource("s3")  # mytype: boto3.resources.factory.s3.ServiceResource
bucket = s3.Bucket(bucket_name)  # mytype: boto3.resources.factory.s3.Bucket
bucket.download_file(key, local)

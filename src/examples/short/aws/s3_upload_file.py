"""
This is an example of how to upload a single file to s3
"""

import boto3

bucket_name = "litebc-upload"
key = "test.txt"
local = "/etc/passwd"

s3 = boto3.resource("s3")  # mytype: boto3.resources.factory.s3.ServiceResource
bucket = s3.Bucket(bucket_name)  # mytype: boto3.resources.factory.s3.Bucket
bucket.upload_file(local, key)

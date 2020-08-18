"""
This is an example of how to download a single file from s3
This is how to download the file to a local file, not to RAM.
"""

import boto3

bucket_name = 'bucket_name'
key = 'key_name'
local = '/tmp/details.txt'

s3 = boto3.resource('s3')  # type: boto3.resources.factory.s3.ServiceResource
bucket = s3.Bucket(bucket_name)  # type: boto3.resources.factory.s3.Bucket
bucket.download_file(key, local)

"""
This is an example of how to download an object from s3 directly to a file handle.

References:
- https://www.radishlogic.com/aws/s3/how-to-download-files-from-s3-bucket-using-boto3-and-python/
"""

import boto3

bucket_name = "litebc-upload"
key = "10k/2023-05-02/18934974-d25a-4895-8208-b707ee2d586c_0/0/recording_id.txt"
local = "/tmp/recording_id.txt"

s3_client = boto3.client('s3')
with open(local, 'wb') as file:
    s3_client.download_fileobj(
        Bucket=bucket_name,
        Key=key,
        Fileobj=file
    )

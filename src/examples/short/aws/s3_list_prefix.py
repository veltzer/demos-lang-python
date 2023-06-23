"""
An example about how to connect to s3 and iterate files
in some "sub folder" of s3.

The credentials for this are NOT stored in this script
but rather are in ~/.aws/credentials.

References:
- http://boto.cloudhackers.com/en/latest/
- http://boto.cloudhackers.com/en/latest/ref/
"""

import boto3

do_print = True

bucket_name = "bucket_name"
folder = "folder"

s3 = boto3.resource("s3")
bucket = s3.Bucket(bucket_name)
key_list = bucket.list(folder)
file_num = 0
for key in key_list:
    print(f"got [{key.name}]")
    file_num += 1
print(f"got [{file_num}] files...")

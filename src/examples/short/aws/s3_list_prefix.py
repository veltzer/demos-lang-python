"""
An example about how to connect to s3 and iterate files
in some "sub folder" of s3.

The credentials for this are NOT stored in this script
but rather are in ~/.aws/credentials.

References:
- http://boto.cloudhackers.com/en/latest/
- http://boto.cloudhackers.com/en/latest/ref/
"""
import itertools
import boto3

do_print = True

bucket_name = "litebc-upload"
folder = "/"

s3 = boto3.resource("s3")
bucket = s3.Bucket(bucket_name)
file_num = 0
for key in itertools.islice(bucket.objects.all(), 10):
    print(f"got [{key.key}]")
    file_num += 1
print(f"got [{file_num}] files...")

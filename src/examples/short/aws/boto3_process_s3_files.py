"""
An example about how to connect to s3 and iterate files
in some "folder" of s3 using the 'boto3' module.

The credentials for this are NOT stored in this script
but rather are in ~/.aws/credentials.

References:
- https://boto3.readthedocs.io/en/latest/
- http://stackoverflow.com/questions/36205481/read-file-content-from-s3-bucket-with-boto3
"""

import codecs
import locale

import boto3
import tqdm

do_count_lines = True
bucket_name = "bucket_name"
folder = "folder"

s3 = boto3.resource("s3")
bucket = s3.Bucket(bucket_name)
# this will give you all objects in the bucket
# gen = bucket.objects.all()
# this will give you only the objects in one folder
gen = bucket.objects.filter(Prefix=folder)
file_num = 0
for object_summary in gen:
    print(f"doing [{object_summary.key}]")
    file_num += 1
    if do_count_lines:
        stream = object_summary.get()['Body']
        # stream = io.BufferedReader(stream)
        # stream = io.TextIOWrapper(stream)
        stream = codecs.getreader(encoding=locale.getpreferredencoding())(stream)
        lines = 0
        for line in tqdm.tqdm(stream):
            # print(line, end="")
            lines += 1
        print(f"got [{lines}] lines...")
print(f"got [{file_num}] files...")

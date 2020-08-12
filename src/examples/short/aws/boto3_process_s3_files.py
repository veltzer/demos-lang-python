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

import boto3
import tqdm

do_count_lines = True
bucket_name = 'twiggle-click-streams'
folder = 'mft.similarweb.com/'

s3 = boto3.resource('s3')
bucket = s3.Bucket('twiggle-click-streams')
# this will give you all objects in the bucket
# gen = bucket.objects.all()
# this will give you only the objects in one folder
gen = bucket.objects.filter(Prefix=folder)
file_num = 0
for object_summary in gen:
    print('doing [{0}]'.format(object_summary.key))
    file_num += 1
    if do_count_lines:
        stream = object_summary.get()['Body']
        # stream = io.BufferedReader(stream)
        # stream = io.TextIOWrapper(stream)
        stream = codecs.getreader(encoding='utf-8')(stream)
        lines = 0
        for line in tqdm.tqdm(stream):
            # print(line, end='')
            lines += 1
        print('got [{0}] lines...'.format(lines))
print('got [{0}] files...'.format(file_num))

#!/usr/bin/env python

"""
This is an example of how to download a single file from s3

This is how to download the file to a local file, not to RAM.
"""

import boto3

do_count_lines = True
bucket_name = 'twiggle-click-streams'
key = 'catalogs/flipkart/catalog/2016-11-23/compressed/details.txt'
local = '/tmp/details.txt'

s3 = boto3.resource('s3')  # type: boto3.resources.factory.s3.ServiceResource
bucket = s3.Bucket('twiggle-click-streams')  # type: boto3.resources.factory.s3.Bucket
bucket.download_file(key, local)

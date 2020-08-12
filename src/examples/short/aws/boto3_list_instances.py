"""
This is an example of how to list instances using the python boto3 library

References:
- http://boto3.readthedocs.io/en/latest/guide/migrationec2.html
"""

import boto3

ec2 = boto3.resource('ec2')  # type: boto3.resources.factory.ec2.ServiceResource
instances = ec2.instances.filter(
    Filters=[
        {'Name': 'instance-state-name', 'Values': ['running']},
        {'Name': 'tag:Owner', 'Values': ['mark@twiggle.com']},
    ]
)
for instance in instances:
    print(instance.id)
    print(instance.instance_type)
    print(instance.public_dns_name)
    print(instance.key_name)

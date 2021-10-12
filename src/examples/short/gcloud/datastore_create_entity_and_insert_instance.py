"""
This is a simple example of how to enter data into a google
cloud store

References:
- https://cloud.google.com/datastore/docs/datastore-api-tutorial
"""

# pylint: disable=no-name-in-module
from google.cloud import datastore

datastore_client = datastore.Client()
kind = 'kind_name'
name = 'A one to many mapping'
entity_key = datastore_client.key(kind, name)
instance = datastore.Entity(key=entity_key)
instance['description'] = "this is a description"
instance['list'] = list(range(10))
datastore_client.put(instance)
print(f'Saved {instance.key.name}')

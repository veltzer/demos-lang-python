"""
This is a simple example of how to enter data into a google
cloud store

References:
- https://cloud.google.com/datastore/docs/datastore-api-tutorial
"""

from google.cloud import datastore

datastore_client = datastore.Client()
kind = 'Nikud'
name = 'A one to many mapping'
entity_key = datastore_client.key(kind, name)
instance = datastore.Entity(key=entity_key)
instance['description'] = "this is a description"
instance['list'] = list(range(10))
datastore_client.put(instance)
print('Saved {}'.format(instance.key.name))

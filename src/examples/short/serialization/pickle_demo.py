"""
Demo of the 'pickle' module for serialization and deserialization
"""

import pickle

# .p is for 'pickle'
filename = '/tmp/serialized.p'

favorite_color = {"lion": "yellow", "kitty": "red"}

with open(filename, "wb") as file_handle:
    pickle.dump(favorite_color, file_handle)

with open(filename, "rb") as file_handle:
    new_dict = pickle.load(file_handle)

assert favorite_color == new_dict

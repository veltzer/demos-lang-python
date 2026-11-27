"""
An example of how to validate a YAML document using the jsonschema module.

References:
- https://stackoverflow.com/questions/3262569/validating-a-yaml-document-in-python
"""

import yaml
from jsonschema import validate

schema = """
type: object
properties:
  testing:
    type: array
    items:
      enum:
        - this
        - is
        - a
        - test
"""

good_instance = """
testing: ["this", "is", "a", "test"]
"""

validate(yaml.load(good_instance, Loader=yaml.SafeLoader), yaml.load(schema, Loader=yaml.SafeLoader))  # passes

# Now lets try a bad instance...

bad_instance = """
testing: ["this", "is", "a", "bad", "test"]
"""

# this raises a ValidationError, which is the point of the example
validate(yaml.load(bad_instance, Loader=yaml.SafeLoader), yaml.load(schema, Loader=yaml.SafeLoader))

"""
An example of how to validate a YAML document using the jsonschema module.

References:
- https://stackoverflow.com/questions/3262569/validating-a-yaml-document-in-python
"""

import yaml
from jsonschema import validate
from jsonschema.exceptions import ValidationError

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

try:
    validate(yaml.load(bad_instance, Loader=yaml.SafeLoader), yaml.load(schema, Loader=yaml.SafeLoader))
except ValidationError as e:
    raise e

"""
This example shows how to load two yamls from one file (using the "---" separator)

References:
- https://stackoverflow.com/questions/14359557/reading-yaml-file-with-python-results-in-yaml-composer-composererror-expected-a
"""

import yaml

with open("data/yaml/two_documents_in_one_file.yaml") as stream:
    try:
        documents = yaml.safe_load_all(stream)
        for document in documents:
            print(document)
    except yaml.YAMLError as exc:
        print(exc)

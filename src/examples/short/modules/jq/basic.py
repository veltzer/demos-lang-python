""" basic.py """

import jq

json_data = {
    "resources": [
        {"url": "https://example.com/1", "other_data": "some value"},
        {"url": "https://example.com/2", "other_data": "another value"},
        {"url": "https://example.com/3", "other_data": "more value"}
    ]
}

# pylint: disable=c-extension-no-member
urls = jq.compile(".resources[].url").input(json_data).all()
print(urls)  # Output: ['https://example.com/1', 'https://example.com/2', 'https://example.com/3']

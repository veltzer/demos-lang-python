import sys
import yaml

dict_file = {
    "sports":
    [
        "soccer",
        "football",
        "basketball",
        "cricket",
        "hockey",
        "table tennis",
    ],
    "countries":
    [
        "Pakistan",
        "USA",
        "India",
        "China",
        "Germany",
        "France",
        "Spain"
    ]
}

documents = yaml.dump(dict_file, sys.stdout)

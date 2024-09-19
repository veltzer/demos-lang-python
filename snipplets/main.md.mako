<%!
    import pydmt.helpers.git
%>${"##"} Number of examples

Currently there are ${pydmt.helpers.git.count_files("src/**/*.py")} examples in this repo.

${"##"} How to use the examples

* Create a virtual env:

```bash
virtualenv my_venv
```

* Enter your virtual env:

```
source my_venv/bin/activate
```

* Install the requirements:

```
pip install -r requirements.txt
```

* Pick an example and run it:

```bash
python src/examples/short/modules/pandas/basic.py
```

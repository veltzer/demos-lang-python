<%!
	import config.python
%>name: build
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    container: ${"${{ matrix.container }}"}
    strategy:
      matrix:
        container: ${config.python.test_container}
        python-version: ${config.python.test_python}
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python ${"${{ matrix.python-version }}"}
      uses: actions/setup-python@v2
      with:
        python-version: ${"${{ matrix.python-version }}"}
    - name: Install OS packages
      run: python -m scripts.install
    - name: Install python dependencies
      run: |
        python -m pip install --upgrade pip
        python -m pip install -r requirements.txt
    - name: Build
      run: make

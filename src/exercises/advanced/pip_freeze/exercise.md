For the previous exercise we needed two external python modules:
	- flask
	- requests
We are now going to see how to freeze our requirements so that we will always install the exact
version of the packages we want.

1. Create virtual envrionment (using the virtualenv command line tool)
	If you don't have a tool called "virtualenv" install it via pip:
		$ pip install virtualenv
2. Write a "requirements.txt" file for your project.
	It should have both modules listed as requirements.
3. Install the requirements into your newly created virtualenv:
	$ pip install -r requirements.txt
4. use "pip freeze" to create a frozen version of your requirements, with precice version numbers.
	Store the freeze. in requirements.freeze.txt
5. Demonstrate how you create a new virtualenv, and install requirements from the frozen version.

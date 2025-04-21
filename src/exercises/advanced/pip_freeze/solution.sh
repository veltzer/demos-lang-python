#!/bin/bash -ex
# cleanup
rm -rf venv venv.frozen
# create a new virtual env
virtualenv venv
# enter the new virtual env
source venv/bin/activate
# show that I dont have flask and requests
pip show flask requests || true
# install flask and requests WITHOUT specifying version numbers
pip install -r requirements.txt
echo "these are the versions of flask and requests after installation"
pip show flask requests
# create a freeze file using pip freeze
pip freeze > requirements.freeze.txt
# create a new virtual env
virtualenv venv.frozen
# enter the new virtual env
source venv.frozen/bin/activate
# show that I dont have flask and requests
pip show flask requests || true
# install flask and requests according to the frozen requements 
pip install -r requirements.freeze.txt
echo "these are the versions of flask and requests after installation"
pip show flask requests

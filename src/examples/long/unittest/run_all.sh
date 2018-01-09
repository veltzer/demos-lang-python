#!/bin/sh

for x in `find . -name "*Test.py"`; do
	echo ${x}
	python3 ${x}
done

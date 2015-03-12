# 
# TimeToken
# 
# Author: José David Fernández Curado
# Email: david@dialeti.co
# 
# This project is based on Django's password token generator
# 

SHELL := /bin/bash

develop install:
	python setup.py "$@"
clean:
	rm -rf bdist dist sdist build
	find . -iname '*.egg' | xargs rm -rf
	find . -iname '*.egg-*' | xargs rm -rf
	
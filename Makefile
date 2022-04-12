MAKEFLAGS += --silent
#####################################################################

PROJECT_NAME := tzfzf

#####################################################################

PROJECT_ROOT := $(shell pwd)

#####################################################################

default: build-all

build-all:
	$(PROJECT_ROOT)/setup.py build_scripts
	$(PROJECT_ROOT)/setup.py build
	$(PROJECT_ROOT)/setup.py sdist

clean:
	rm -rf $(PROJECT_ROOT)/dist

clean-all: clean
	rm -rf $(PROJECT_ROOT)/build
	rm -rf $(PROJECT_ROOT)/tzfzf.egg-info

uninstall:
	yes | pip uninstall $(PROJECT_NAME)

install:
	pip install $(shell ls ./dist/*)

reinstall: uninstall clean-all build-all install

#####################################################################

#!/usr/bin/env python
from setuptools import setup, find_packages

from tzfzf import __version__, __author__


with open('README.md', 'r', encoding='utf-8') as readme:
    long_description = readme.read()
    long_description_content_type = 'text/markdown'

setup(
    name='tzfzf',
    version=__version__,
    description='a terminal CLI / API for quick cross-timezone lookups',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/wrynegade/tzfzf',
    author=__author__,
    author_email='yage@yage.io',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'python-dateutil',
        'pytz',
        ],
    classifiers=[
        'Programming Language :: Python :: 3 :: Only',
        ],
    entry_points={
        'console_scripts': [
            'tzfzf = tzfzf.cli:main',
            ],
        },
    )

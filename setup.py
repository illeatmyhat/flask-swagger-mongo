# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "app"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

setup(
    name=NAME,
    version=VERSION,
    description="flask-restplus-mongo",
    author_email="",
    url="",
    keywords=["flask-restplus-mongo"],
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': ['app=app.__main__:main']}
)


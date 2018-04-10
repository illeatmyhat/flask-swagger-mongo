# coding: utf-8

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
    description="flask-swagger-mongo",
    # author_email="",
    # url="",
    keywords=["flask-swagger-mongo"],
    # include_package_data=True,
    packages=find_packages(),
    entry_points={
        'console_scripts': ['app=app.__main__:main']}
)


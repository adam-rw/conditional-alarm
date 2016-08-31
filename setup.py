# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='conditional_alarm',
    version='0.0.1',
    description='Conditional Alarm Clock',
    long_description=readme,
    author='Adam Williams',
    author_email='adam.williams@linux.com',
    url='https://github.com/rofl-lol/conditional-alarm',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)


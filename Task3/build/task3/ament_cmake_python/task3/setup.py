from setuptools import find_packages
from setuptools import setup

setup(
    name='task3',
    version='0.0.0',
    packages=find_packages(
        include=('task3', 'task3.*')),
)

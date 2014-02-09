from setuptools import setup, find_packages

setup(
    name="dominoscli",
    version="0.0.1",
    packages=find_packages(),
    author="Rick van Biljouw",
    author_email="rick@ondemand.io",
    scripts = [
        'bin/dominos.py'
    ],
    data_files = [
    ],
)

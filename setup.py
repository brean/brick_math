#!/usr/bin/env python3
from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="brick_math",
    description="Python library to make calculations with bricks easier.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brean/brick_math",
    version="0.1",
    license="BSD-3",
    author="Andreas Bresser",
    packages=find_packages(),
    tests_require=[],
    package_data={},
    install_requires=[
        'argcomplete',
    ]
)

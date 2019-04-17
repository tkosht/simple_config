# -*- coding: utf-8 -*-

import pathlib
import setuptools


def get_requirements():
    req = pathlib.Path("requirements.txt")
    libs = [l.rstrip() for l in req.open(mode="r").readlines()]
    return libs


requirements = get_requirements()
readme = pathlib.Path("README.md").open(mode="r").read()


setuptools.setup(
    name='sconfig',
    version="1.0.0",
    author='tkosht',
    author_email='xxx',
    url='https://github.com/tkosht/simple_config.git',
    description='a simple config module',
    long_description=readme,
    license='MIT',

    packages=setuptools.find_packages(exclude=('test', 'examples')),

    zip_safe=True,
    install_requires=requirements,
    extras_require={},
)

# coding=utf-8
from setuptools import find_packages
from setuptools import setup

import os


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


long_description = (
    read('src', 'z3c', 'objpath', 'README.txt')
    + '\n' +
    read('CHANGES.txt')
    + '\n' +
    'Download\n'
    '********\n'
    )

setup(
    name='z3c.objpath',
    version='1.2dev',
    description="Generate and resolve paths to to objects.",
    long_description=long_description,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    keywords='',
    author='Martijn Faassen',
    author_email='faassen@startifact.com',
    license='ZPL',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['z3c'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'zope.interface',
    ],
    entry_points={},
    )

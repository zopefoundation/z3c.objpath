# coding=utf-8
from setuptools import find_packages
from setuptools import setup

import os


def read(*rnames):
    with open(os.path.join(os.path.dirname(__file__), *rnames)) as f:
        return f.read()


long_description = (
    read('src', 'z3c', 'objpath', 'README.rst')
    + '\n' +
    read('CHANGES.rst')
)

setup(
    name='z3c.objpath',
    version='1.2',
    description="Generate and resolve paths to to objects.",
    long_description=long_description,
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'License :: OSI Approved :: Zope Public License',
    ],
    keywords='Zope',
    author='Martijn Faassen',
    author_email='faassen@startifact.com',
    url='https://github.com/zopefoundation/z3c.objpath',
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

import os

from setuptools import setup


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
    version='3.0',
    description="Generate and resolve paths to to objects.",
    long_description=long_description,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'License :: OSI Approved :: Zope Public License',
    ],
    keywords='Zope',
    author='Martijn Faassen',
    author_email='faassen@startifact.com',
    url='https://github.com/zopefoundation/z3c.objpath',
    license='ZPL',
    include_package_data=True,
    zip_safe=False,
    python_requires='>=3.9',
    install_requires=[
        'setuptools',
        'zope.interface',
    ],
    entry_points={},
)

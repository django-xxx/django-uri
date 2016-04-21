# -*- coding: utf-8 -*-
from __future__ import with_statement
from setuptools import setup


version = '1.0.0'


setup(
    name='django-uri',
    version=version,
    keywords='django-uri',
    description='Django URI',
    long_description=open('README.rst').read(),

    url='https://github.com/Brightcells/django-uri',

    author='Hackathon',
    author_email='kimi.huang@brightcells.com',

    packages=['uri', ],
    py_modules=[],
    install_requires=[],

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Office/Business :: Financial :: Spreadsheet',
    ],
)

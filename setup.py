# -*- coding: utf-8 -*-

from setuptools import setup


version = '1.0.2'


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
    install_requires=['django-six'],

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

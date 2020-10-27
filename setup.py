# -*- coding: utf-8 -*-
from io import open
from setuptools import setup

"""
:authors: Duzive
:license: Apache License, Version 2.0, see LICENSE file
:copyright: (c) 2020-2021 Duzive
"""

version = '1.0.0'

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='worldcoin',
    version=version,

    author='Duzive',

    description=(
        u'Это модуль для упрощенной работы с api WorldCoin'
    ),

    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/Duzive/worldcoin',
    download_url=f'https://github.com/Duzive/worldcoin/archive/v{version}.zip',

    license='Apache License, Version 2.0, see LICENSE file',

    packages=['worldcoin'],
    install_requires=['requests'],

    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython',
    ]
)

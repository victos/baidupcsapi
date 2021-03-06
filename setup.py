#!/usr/bin/env python3
# coding=utf-8

__title__ = 'baidupcsapi'
__version__ = '0.9.3'
__author__ = 'ly0, mozillazg101'
__license__ = 'MIT'

from setuptools import setup


requirements = [
    'requests>=1.1.0',
    'requests_toolbelt>=0.1.2',
    'rsa>=3.1.4'
]
packages = [
    'baidupcsapi',
]

setup(
    name='baidupcsapi',
    version=__version__,
    description='百度网盘API',
    url='https://github.com/ly0/baidupcsapi',
    download_url='https://github.com/ly0/baidupcsapi',
    author=__author__,
    author_email='latyas@gmail.com,mozillazg101@gmail.com',
    license=__license__,
    packages=packages,
    package_data={'': ['LICENSE.txt']},
    package_dir={'baidupcsapi': 'baidupcsapi'},
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
    ],
    keywords='百度网盘, 百度云, API',
)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import ast
import io
import re

from setuptools import setup, find_packages

with io.open('README.md', 'rt', encoding="utf8") as f:
    readme = f.read()

_description_re = re.compile(r'description\s+=\s+(?P<description>.*)')

with open('lektor_html_pretify.py', 'rb') as f:
    description = str(ast.literal_eval(_description_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    author='L3D',
    author_email='l3d@c3woc.de',
    description=description,
    keywords='Lektor plugin',
    license='MIT',
    long_description=readme,
    long_description_content_type='text/markdown',
    name='lektor-html-pretify',
    packages=find_packages(),
    py_modules=['lektor_html_pretify'],
    url='https://github.com/chaos-bodensee/lektor-html-pretify',
    version='1.0.7',
    classifiers=[
        'Framework :: Lektor',
        'Environment :: Plugins',
    ],
    entry_points={
        'lektor.plugins': [
            'html-pretify = lektor_html_pretify:HtmlPretifyPlugin',
        ]
    },
    install_requires=['bs4']
)

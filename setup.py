#!/usr/bin/env python
""" 
  Package setup/installation for lambdata_edc
"""

import setuptools

REQUIRED = [
    'numpy',
    'pandas'
    ]

with open('README.md','r') as fh:
  LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name='lambdata-edc',
    version='1.0.0' ,
    author='Ed Chin',
    description="utility library",
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/ed-chin-git/lambdata',
    packages=setuptools.find_packages(),
    python_requires='>=3.5',
    install_requires=REQUIRED,
    classifiers=[

        "Programming Language :: Python :: 3",

        "License :: OSI Approved :: MIT License",

        "Operating System :: OS Independent",]
     )

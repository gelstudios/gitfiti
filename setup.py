#!/usr/bin/env python
from setuptools import setup, find_packages

import gitfiti

requires = []

setup_options = dict(
    name='gitfiti',
    version=gitfiti.__version__,
    description='Carefully crafted graffiti '
                'in a github commit history calendar.',
    long_description='See docs at https://github.com/gelstudios/gitfiti',
    author='gelstudios',
    author_email='',
    url='https://github.com/gelstudios/gitfiti',
    packages=find_packages('.'),
    package_dir={'gitfiti': 'gitfiti'},
    install_requires=requires,
    license="MIT",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    entry_points={
        'console_scripts': [
            'gitfiti=gitfiti.main:main'
        ]
    }
)

setup(**setup_options)

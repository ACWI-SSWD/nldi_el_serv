#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

# requirements = ['Click>=7.0', ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Richard McDonald",
    author_email='rmcd@usgs.gov',
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: CC0 1.0 Universal',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.8',
    ],
    description="NLDI Elevation Services",
    entry_points={
        'console_scripts': [
            'nldi_el_serv=nldi_el_serv.cli:main',
        ],
    },
    install_requires=requirements,
    license="CC0 1.0 Universal public domain dedication",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='nldi_el_serv',
    name='nldi_el_serv',
    packages=find_packages(include=['nldi_el_serv', 'nldi_el_serv.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/ACWI-SSWD/nldi_el_serv',
    version='0.1.2',
    zip_safe=False,
)

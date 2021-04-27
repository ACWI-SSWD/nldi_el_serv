#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

# with open('requires.txt') as f:
#     requirements = f.read().splitlines()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0',
                'pygeohydro==0.10.2',
                'py3dep==0.10.1',
                'pygeoogc==0.10.1',
                'pygeoutils==0.10.1',
                'pynhd==0.10.1',
                'shapely',
                'dataretrieval',
                'folium',
                'lxml',
                'xarray',
                'scipy',
                'dask',
                'netcdf4',
                'bottleneck',
                'geopandas',
                'numba']

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Richard McDonald",
    author_email='rmcd@usgs.gov',
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
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
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='nldi_el_serv',
    name='nldi_el_serv',
    packages=find_packages(include=['nldi_el_serv', 'nldi_el_serv.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/ACWI-SSWD/nldi_el_serv',
    version='0.1.9',
    zip_safe=False,
)

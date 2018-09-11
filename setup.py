#!/usr/bin/env python
from setuptools import find_packages
from distutils.core import setup
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

package_name = "q-dbt"
package_version = "0.11.0"

setup(
    name=package_name,
    version=package_version,
    description=description,
    long_description_content_type=description,
    author="Fishtown Analytics",
    author_email="info@fishtownanalytics.com",
    url="https://github.com/managedbyq/q-dbt",
    packages=find_packages(),
    package_data={
        'q-dbt': [
            'include/index.html',
            'include/global_project/dbt_project.yml',
            'include/global_project/docs/*.md',
            'include/global_project/macros/*.sql',
            'include/global_project/macros/**/*.sql',
            'include/global_project/macros/**/**/*.sql',
        ]
    },
    test_suite='test',
    entry_points={
        'console_scripts': [
            'dbt = dbt.main:main',
        ],
    },
    scripts=[
        'scripts/dbt',
    ],
    install_requires=[
        'python-dateutil<2.7.0',
        'freezegun==0.3.9',
        'Jinja2>=2.8',
        'PyYAML>=3.11',
        'psycopg2>=2.7.5,<2.8',
        'sqlparse==0.2.3',
        'networkx==1.11',
        'minimal-snowplow-tracker==0.0.1',
        'snowflake-connector-python>=1.4.9',
        'requests>=2.18.0,<3',
        'colorama==0.3.9',
        'google-cloud-bigquery>=1.0.0,<2',
        'agate>=1.6,<2',
        'rollbar==0.13.17',
        'jsonschema==2.6.0',
        'boto3>=1.6.23,<1.8.0',
        'botocore>=1.9.23,<1.11.0',
    ]
)

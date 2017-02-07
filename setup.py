"""
emdata-clean
-----

This packages is going to do the job of cleaning the ES & mongoDB.

.. code:: python

    emdata_clean -f config.yaml del --filter '{"hospitalId": 1}'
"""
from setuptools import setup

setup(
    name='emdata-clean',
    version='1.0',
    packages=['emdata_clean'],
    install_requires=[
        'Click',
        'progress',
        'pymongo',
        'pyyaml',
        'elasticsearch>=2.0.0,<3.0.0',
        'PyMySQL',
    ],
    entry_points='''
        [console_scripts]
        emdata_clean=emdata_clean.main:cli
    '''
)

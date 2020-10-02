# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, '')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')

setup(
    long_description=readme,
    name='price_prediction_model',
    version='1.0.1',
    description='End to end lightGBM regression model to predict house prices in Beijing',
    python_requires='==3.*,>=3.7.0',
    author='Bowen',
    packages=[
        'price_prediction_model', 'price_prediction_model.config',
        'price_prediction_model.features', 'price_prediction_model.model',
        'price_prediction_model.preprocessing', 'price_prediction_model.utils'
    ],
    package_dir={"price_prediction_model": ""},
    package_data={
        "price_prediction_model": [
            "*.lock", "*.md", "*.toml", "data/*.csv",
            "trained_model_files/*.pkl"
        ]
    },
    install_requires=[
        'lightgbm', 'matplotlib', 'numpy', 'pandas', 'poetry-version',
        'seaborn', 'sklearn'
    ],
    extras_require={"dev": ["black==19.3b0", "nb-black", "pytest"]},
)

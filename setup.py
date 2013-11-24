#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = "django-opening-hours",
    version = "1.4.2",
    url = 'https://github.com/ondrejsika/django-opening-hours/',
    license = 'MIT',
    description = "Opening hours field and admin widget",
    author = 'Ondrej Sika',
    author_email = 'ondrej@ondrejsika.com',
    packages = find_packages(),
    requires = [],
    include_package_data = True,
    zip_safe = False,
)

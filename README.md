django-opening-hours
====================

Model and andmin for management opening hours

### Authors
*  Ondrej Sika, <http://ondrejsika.com>, dev@ondrejsika.com

### Source
* Python Package Index: <http://pypi.python.org/pypi/django-opening-hours>
* GitHub: <https://github.com/sikaondrej/django-opening-hours>

Documentation
-------------

### Instalation
Instalation is very simple over pip.

    pip install django-opening-hours

### Usage
settings.py

    INSTALLED_APPS += ("opening_hours", )

myapp/models.py

    from django.db import models
    from opening_hours.db_fields import OpeningHoursField

    class Store(model.Model):
        name = models.CharField(max_length=255)
        opening_hours = OpeningHoursField()
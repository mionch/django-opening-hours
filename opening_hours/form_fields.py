from django import forms
from django.db.models import get_model

from widgets import OpeningHoursWidget

from django.forms import widgets

class OpeningHoursField(forms.CharField):
    def __init__(self, **kwargs):
        defaults = {
            'widget': OpeningHoursWidget(),
        }
        defaults.update(kwargs)
        return super(self.__class__, self).__init__(**defaults)

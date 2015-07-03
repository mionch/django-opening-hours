# -*- coding: utf-8 -*-
from django import forms
from django.core.exceptions import ValidationError

from widgets import OpeningHoursWidget

import json

class OpeningHoursField(forms.CharField):
    def __init__(self, **kwargs):
        defaults = {
            'widget': OpeningHoursWidget(),
        }
        defaults.update(kwargs)
        return super(OpeningHoursField, self).__init__(**defaults)

    def clean(self, value):
        def is_time(s):  # XXX:
            import re
            if not s:
                return True
            if re.match(r"\d+:\d+", s) and re.match(r"\d+:\d+", s).group() == s:
                return True
            return False

        data = json.loads(value)
        for day in ["mo", "tu", "we", "th", "fr", "sa", "su"]:
            for d in data[day]:
                if not is_time(d[0]) or not is_time(d[1]):
                    raise ValidationError(u"Wprowadzono niepoprawny format godziny - dopuszczalne puste wartości lub "
                                           u"godzina w formacie HH:MM")
        print json.dumps(data)
        return json.dumps(data)
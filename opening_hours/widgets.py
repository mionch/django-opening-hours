from django.forms.widgets import Widget

from django.template import loader
from django.utils.safestring import mark_safe
from django.conf import settings

import random

class OpeningHoursWidget(Widget):
    is_required = False
    def render(self, name, value, attrs=None):
        if not value:
            value = '{"mo":[["", ""]], "tu":[["", ""]], "we":[["", ""]], "th":[["", ""]], "fr":[["", ""]], "sa":[["", ""]], "su":[["", ""]]}'
        return mark_safe(loader.render_to_string("opening_hours/widget.html", {
            "value": value,
            "name": name,
            "STATIC_URL": settings.STATIC_URL,
            "prefix": str(random.randint(11111111, 99999999)),
        }))

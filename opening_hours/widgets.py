from django.forms.widgets import Widget

from django.template import loader
from django.utils.safestring import mark_safe
from django.conf import settings

class OpeningHoursWidget(Widget):
    is_required = False
    def render(self, name, value, attrs=None):
        return mark_safe(loader.render_to_string("opening_hours_field/widget.html", {
            "value": value,
            "STATIC_URL": settings.STATIC_URL,
        }))

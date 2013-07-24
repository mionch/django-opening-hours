from django.forms.widgets import Widget

from django.template import loader
from django.utils.safestring import mark_safe
from django.conf import settings


class OpeningHoursWidget(Widget):
    is_required = False
    template = "opening_hours/widget.html"
    def render(self, name, value, attrs=None):
        if not value:
            value = '{"first_day": "mo", "mo": [], "tu":[], "we":[], "th":[], "fr":[], "sa":[], "su":[], "mo_note": "", "tu_note": "", "we_note":"", "th_note":"", "fr_note":"", "sa_note":"", "su_note":"" }'
        return mark_safe(loader.render_to_string(self.template, {
            "value": value,
            "name": name,
            "STATIC_URL": settings.STATIC_URL,
        }))

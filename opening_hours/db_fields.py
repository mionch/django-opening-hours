from django.db import models
from django.utils.six import with_metaclass
import form_fields
import widgets
import json


DEFAULT_OPENING_HOURS_JSON = '{"we_note": "false", "fr_note": "false", "fr": [], "su_note": "false", "mo_note": "false", "mo": [], "tu": [], "th_note": "false", "we": [], "su": [], "tu_note": "false", "th": [], "sa_note": "false", "sa": [], "first_day": "mo"}'

class OpeningHoursField(with_metaclass(models.SubfieldBase, models.Field)):
    def __init__(self, *args, **kwargs):
        kwargs.update({
            'default': DEFAULT_OPENING_HOURS_JSON,
        })
        return super(OpeningHoursField, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        return "TextField"

    def to_python(self, value):
        if type(value) == str or type(value) == unicode:
            return json.loads(value)
        else:
            return value

    def get_prep_value(self, value):
        if type(value) != str or type(value) != unicode:
            return json.dumps(value)
        else:
            return value

    def formfield(self, **kwargs):
        defaults = {
            'form_class': form_fields.OpeningHoursField,
            'widget': widgets.OpeningHoursWidget,
        }
        defaults.update(kwargs)
        return super(OpeningHoursField, self).formfield(**defaults)

    def south_field_triple(self):
        from south.modelsinspector import introspector
        field_class = "django.db.models.fields.TextField"
        args, kwargs = introspector(self)
        return (field_class, args, kwargs)

from django.db import models

import form_fields
import widgets

class OpeningHoursField(models.Field):
    def get_internal_type(self):
        return "TextField"

    def formfield(self, **kwargs):
        defaults = {
            'form_class': form_fields.OpeningHoursField,
            'widget': widgets.OpeningHoursWidget,
        }
        defaults.update(kwargs)
        return super(OpeningHoursField, self).formfield(**defaults)

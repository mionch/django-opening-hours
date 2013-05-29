from django.db import models

import form_fields
import widgets

class OpeningHoursField(models.Field):
    def formfield(self, **kwargs):
        defaults = {
            'form_class': form_fields.OpeningHoursField,
            'widget': widgets.OpeningHoursWidget,
        }
        defaults.update(kwargs)
        return super(OpeningHoursField, self).formfield(**defaults)
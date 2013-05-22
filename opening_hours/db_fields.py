from django.db import models

import form_fields

class OpeningHoursField(models.Field):
    def formfield(self, **kwargs):
        defaults = {
            'form_class': form_fields.OpeningHoursField,
        }
        defaults.update(kwargs)
        return super(self.__class__, self).formfield(**defaults)
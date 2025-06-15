from typing import Any, Dict, List, Tuple

from django.db import models
from django.utils import timezone

from estate_agency.estate_agency_apps.common.types import DjangoModelType

def model_update(*, instance, fields, data, auto_updated_at=True):
    print(fields, 'eee111111111111',data)
    has_updated = False
    m2m_data = {}
    fkey = {}
    update_fields = []

    model_fields = {field.name: field for field in instance._meta.get_fields()}
    for field in fields:
        if field not in data:
            continue
        model_field = model_fields.get(field)

        assert model_field is not None, f'{field} is not part of {instance.__class__.__name__} fields'

        if isinstance(model_field, models.ManyToManyField):
            m2m_data[field] = data[field]

        if getattr(instance, field) != data[field]:
            has_updated = True
            update_fields.append(field)
            setattr(instance, field, data[field])

    if has_updated:
        if auto_updated_at:
            if 'updated_at' in model_fields and 'updated_at' not in update_fields:
                update_fields.append('updated_at')
                isinstance.updated_at = timezone.now()
        instance.full_clean()
        instance.save(update_fields=update_fields)

    for field_name, value in m2m_data.items():
        related_manager = getattr(instance, field_name)
        related_manager.set(value)

        # Still not sure about this.
        # What if we only update m2m relations & nothing on the model? Is this still considered as updated?
        has_updated = True

    return instance, has_updated























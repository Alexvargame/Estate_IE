from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.http import Http404
from django.shortcuts import get_object_or_404

def make_mock_object(**kwargs):
    return type('', (object,), kwargs)

def get_object(model_or_queryset, **kwargs):
    try:
        return get_object_or_404(model_or_queryset, **kwargs)
    except Http404:
        return None

def assert_settings(required_settings, error_message_prefix=''):
    not_present = []
    values = {}

    for required_setting in required_settings:
        if not hasattr(settings, required_setting):
            not_present.append(required_setting)
            continue
        values[required_setting] = getattr(settings, required_setting)
        if not_present:
            if not error_message_prefix:
                error_message_prefix = "Required settings not found."

            stringified_not_present = ", ".join(not_present)

            raise ImproperlyConfigured(f"{error_message_prefix} Could not find: {stringified_not_present}")

        return values







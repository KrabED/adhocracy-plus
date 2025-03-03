from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def settings_value(name):
    return getattr(settings, name, "")

import os
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(default=os.environ.get("DATABASE_URL"))
}


WSGI_APPLICATION = 'adhocracy_plus.wsgi.application'

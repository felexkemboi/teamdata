"""
WSGI config for team project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

"""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "team.settings")

application = get_wsgi_application()"""

"""

from whitenoise.django import DjangoWhiteNoise

application = DjangoWhiteNoise(application)
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
"""
import os
"""
from whitenoise import WhiteNoise"""
from django.core.wsgi import get_wsgi_application
"""
from whitenoise.django import DjangoWhiteNoise"""


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "team.settings")
application = get_wsgi_application()
"""application = WhiteNoise(application)"""
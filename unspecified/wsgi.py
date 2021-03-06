import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "unspecified.settings")

from whitenoise import WhiteNoise
application = get_wsgi_application()
application = WhiteNoise(application)
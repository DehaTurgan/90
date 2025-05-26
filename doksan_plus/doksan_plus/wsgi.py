"""
WSGI config for doksan_plus project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from skorlar import app  # Uygulama adını doğru yaz!

if _name_ == "_main_":
    app.run()

# Gunicorn bunu arıyor
application = app

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'doksan_plus.settings')

application = get_wsgi_application()



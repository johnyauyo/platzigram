"""

Archivo usado para el deployment en producción
y es la interfaz WSGI con nuestro proyecto de Django
cuando el servidor esta corriendo en producción

WSGI config for platzigram project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'platzigram.settings')

application = get_wsgi_application()

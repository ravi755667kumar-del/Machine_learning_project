"""
WSGI config for my_django_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# This points the web server to your specific settings file
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_django_project.settings')

# This creates the actual application object the server talks to
application = get_wsgi_application()
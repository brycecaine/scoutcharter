"""
WSGI config for scoutcharter project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
# GETTING-STARTED: change 'scoutcharter' to your project name:
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scoutcharter.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

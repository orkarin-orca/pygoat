"""
ASGI config for pygoat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
response = subprocess.run(create_mr_command, shell=True, capture_output=True, text=True)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pygoat.settings')

application = get_asgi_application()

"""
WSGI config for oasis project.
"""

import os
import sys

# Ajouter le chemin du projet
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oasis.settings')

application = get_wsgi_application()

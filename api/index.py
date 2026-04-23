import os
import sys
from pathlib import Path

# Add the project root directory to Python path
project_root = str(Path(__file__).resolve().parent.parent)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Set Django settings module BEFORE importing Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'banking_management_system.settings')

import django
django.setup()

# Run collectstatic automatically at startup if staticfiles.json is missing
staticfiles_dir = os.path.join(project_root, 'staticfiles')
staticfiles_json = os.path.join(staticfiles_dir, 'staticfiles.json')
if not os.path.isfile(staticfiles_json):
    try:
        from django.core.management import call_command
        call_command('collectstatic', '--noinput', verbosity=0)
    except Exception:
        pass  # Don't crash startup if collectstatic fails

# Get the WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Wrap with WhiteNoise to serve static files from the serverless function
from whitenoise import WhiteNoise
if os.path.isdir(staticfiles_dir):
    application = WhiteNoise(application, root=staticfiles_dir, prefix='static')

# Vercel expects the WSGI app to be named 'app'
app = application
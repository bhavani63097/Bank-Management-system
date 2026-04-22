import os
import sys
import django
from pathlib import Path

# Add the project directory to the path
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'banking_management_system.settings')

try:
    django.setup()
except Exception as e:
    print(f"Django setup failed: {e}")
    raise

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

# Get the base WSGI application
application = get_wsgi_application()

# Wrap it with WhiteNoise to serve static files
application = WhiteNoise(
    application,
    root=os.path.join(project_dir, 'staticfiles'),
    index_file=True,
    autorefresh=True,
    max_age=31536000,
)

# For Vercel's serverless function handler
app = application
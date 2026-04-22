import os
import sys
from pathlib import Path

# Add the project root directory to Python path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'banking_management_system.settings')

# Get the WSGI application (this also calls django.setup() internally)
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

# Wrap with WhiteNoise to serve static files from the serverless function
from whitenoise import WhiteNoise

staticfiles_dir = os.path.join(Path(__file__).resolve().parent.parent, 'staticfiles')

if os.path.isdir(staticfiles_dir):
    application = WhiteNoise(application, root=staticfiles_dir, prefix='static')

# Vercel expects the WSGI app to be named 'app'
app = application
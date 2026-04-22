import os
import sys
import django
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'banking_management_system.settings')

# Setup Django
django.setup()

# Import after Django setup
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

# Get WSGI application
application = get_wsgi_application()

# Wrap with WhiteNoise for static files
application = WhiteNoise(
    application,
    root=os.path.join(Path(__file__).parent.parent, 'staticfiles'),
    index_file=True,
    mimetypes={'woff2': 'font/woff2'},
)
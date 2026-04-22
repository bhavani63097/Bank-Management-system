import os
import sys
import django

# Add the project directory to the path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'banking_management_system.settings')

try:
    django.setup()
except Exception as e:
    print(f"Django setup failed: {e}")

from django.core.wsgi import get_wsgi_application

app = get_wsgi_application()
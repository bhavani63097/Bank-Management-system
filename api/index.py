import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'banking_management_system.settings')

import django
django.setup()

from django.core.wsgi import get_wsgi_application

app = get_wsgi_application()
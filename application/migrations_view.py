from django.core.management import call_command
from django.http import HttpResponse

def run_migrations(request):
    try:
        call_command('migrate')
        return HttpResponse("Migrations successfully applied to Neon database!")
    except Exception as e:
        return HttpResponse(f"Error applying migrations: {str(e)}")

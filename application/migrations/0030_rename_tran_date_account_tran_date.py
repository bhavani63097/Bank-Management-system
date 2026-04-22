# Replaced with no-op: the column 'Tran_date' was already removed in migration 0028.
# This migration exists only to satisfy the dependency chain.

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0029_account_tran_date'),
    ]

    operations = [
        # No-op: renaming skipped because column does not exist in the current DB.
    ]

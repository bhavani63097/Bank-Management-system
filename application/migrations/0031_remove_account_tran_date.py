# Replaced with no-op: 'tran_date' field was never actually present after migration 0028.
# This migration exists only to satisfy the dependency chain.

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0030_rename_tran_date_account_tran_date'),
    ]

    operations = [
        # No-op: removal skipped because field does not exist in the current DB.
    ]

# Generated by Django 3.2.8 on 1980-01-03 20:07

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0006_auto_19800104_0024'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Add_to_Cart',
            new_name='Cart',
        ),
    ]
# Generated by Django 3.2.8 on 2021-11-05 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_cart_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category_id',
        ),
    ]

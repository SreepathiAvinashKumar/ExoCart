# Generated by Django 4.0 on 2022-02-11 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20211221_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]

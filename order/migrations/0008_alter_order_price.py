# Generated by Django 4.0 on 2022-02-11 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_alter_order_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
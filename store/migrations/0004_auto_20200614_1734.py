# Generated by Django 3.0.7 on 2020-06-14 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20200611_1459'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='adderss',
            new_name='address',
        ),
    ]

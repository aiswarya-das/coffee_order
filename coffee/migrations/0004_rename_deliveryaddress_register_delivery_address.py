# Generated by Django 3.2 on 2021-06-24 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0003_rename_email_register_deliveryaddress'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='deliveryaddress',
            new_name='delivery_address',
        ),
    ]

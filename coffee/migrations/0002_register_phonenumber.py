# Generated by Django 3.2 on 2021-06-24 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='PhoneNumber',
            field=models.IntegerField(default=10),
        ),
    ]

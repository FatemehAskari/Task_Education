# Generated by Django 5.0.6 on 2024-07-14 10:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_alter_application_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='password',
            field=models.CharField(default=datetime.datetime(2024, 7, 14, 10, 57, 35, 34589, tzinfo=datetime.timezone.utc), max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='username',
            field=models.CharField(default=datetime.datetime(2024, 7, 14, 10, 57, 44, 694144, tzinfo=datetime.timezone.utc), max_length=10),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.0.6 on 2024-07-14 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0010_alter_person_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='password',
        ),
        migrations.RemoveField(
            model_name='person',
            name='username',
        ),
    ]

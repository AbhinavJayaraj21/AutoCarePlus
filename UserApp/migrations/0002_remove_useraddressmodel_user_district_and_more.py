# Generated by Django 5.0.1 on 2024-03-05 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraddressmodel',
            name='user_district',
        ),
        migrations.RemoveField(
            model_name='useraddressmodel',
            name='user_state',
        ),
    ]
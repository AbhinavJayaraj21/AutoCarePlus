# Generated by Django 5.0.1 on 2024-05-09 07:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminModel',
            fields=[
                ('admin_id', models.AutoField(primary_key=True, serialize=False)),
                ('admin_name', models.CharField(max_length=10)),
                ('admin_email', models.EmailField(max_length=254)),
                ('admin_phone', models.CharField(max_length=10)),
                ('admin_password', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'admin_table',
            },
        ),
        migrations.CreateModel(
            name='StateModel',
            fields=[
                ('state_id', models.AutoField(primary_key=True, serialize=False)),
                ('state_name', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'state_table',
            },
        ),
        migrations.CreateModel(
            name='DistrictModel',
            fields=[
                ('district_id', models.AutoField(primary_key=True, serialize=False)),
                ('district_name', models.CharField(max_length=100, null=True)),
                ('state_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.statemodel')),
            ],
            options={
                'db_table': 'district_table',
            },
        ),
    ]

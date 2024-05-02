# Generated by Django 5.0.1 on 2024-03-05 04:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AdminApp', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreDetailsModel',
            fields=[
                ('store_date', models.DateField(auto_created=True)),
                ('store_id', models.AutoField(primary_key=True, serialize=False)),
                ('store_name', models.CharField(max_length=100, null=True)),
                ('store_registration_id', models.CharField(max_length=100, null=True)),
                ('store_image', models.ImageField(upload_to='Store/')),
                ('store_phone', models.CharField(max_length=10)),
                ('store_email', models.EmailField(max_length=254)),
                ('store_address', models.CharField(max_length=100, null=True)),
                ('store_district_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.districtmodel')),
            ],
            options={
                'db_table': 'Store_Details_Table',
            },
        ),
    ]

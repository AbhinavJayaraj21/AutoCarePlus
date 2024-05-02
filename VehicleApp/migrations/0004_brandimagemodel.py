# Generated by Django 5.0.1 on 2024-03-06 04:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VehicleApp', '0003_accessoryimagemodel_partsimagemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrandImageModel',
            fields=[
                ('image_id', models.AutoField(primary_key=True, serialize=False)),
                ('brand_image', models.ImageField(upload_to='Vehicle')),
                ('brand_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VehicleApp.vehiclemodel')),
            ],
            options={
                'db_table': 'Brand_Images_Table',
            },
        ),
    ]
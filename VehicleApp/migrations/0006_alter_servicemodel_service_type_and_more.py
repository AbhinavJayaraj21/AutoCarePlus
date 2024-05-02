# Generated by Django 5.0.1 on 2024-03-21 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VehicleApp', '0005_vehicleaccessorymodel_vehicle_accessory_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicemodel',
            name='service_type',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='vehicleaccessorymodel',
            name='vehicle_accessory_category',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='vehicleaccessorymodel',
            name='vehicle_accessory_name',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='vehicleaccessorymodel',
            name='vehicle_accessory_type',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='vehiclepartsmodel',
            name='vehicle_part_category',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='vehiclepartsmodel',
            name='vehicle_part_name',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='vehiclepartsmodel',
            name='vehicle_part_type',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
from django.db import models

from StoreApp.models import *
from AdminApp.models import *


# Create your models here.
# category table
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category_table'


# vehicle table
class VehicleModel(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    vehicle_id = models.AutoField(primary_key=True)
    vehicle_brand = models.CharField(max_length=1000, null=True)
    vehicle_model = models.CharField(max_length=1000, null=True)
    vehicle_year = models.CharField(max_length=4, null=True)
    vehicle_fuel_type = models.CharField(max_length=1000, null=True)
    vehicle_color = models.CharField(max_length=1000, null=True)
    vehicle_variant = models.CharField(max_length=1000, null=True)
    vehicle_budget = models.CharField(max_length=1000, null=True)
    vehicle_body_type = models.CharField(max_length=1000, null=True)
    vehicle_transmission = models.CharField(max_length=1000, null=True)
    vehicle_seating_capacity = models.CharField(max_length=10)
    vehicle_image = models.ImageField(upload_to='Vehicle')

    def __str__(self):
        return self.vehicle_model

    class Meta:
        db_table = 'Vehicle_table'


#  vehicle accessory table
class VehicleAccessoryModel(models.Model):
    vehicle_id = models.ForeignKey(VehicleModel, on_delete=models.CASCADE)
    vehicle_accessory_id = models.AutoField(primary_key=True)
    vehicle_accessory_name = models.CharField(max_length=1000, null=True)
    vehicle_accessory_type = models.CharField(max_length=1000, null=True)
    vehicle_accessory_category = models.CharField(max_length=1000, null=True)
    vehicle_accessory_description = models.CharField(max_length=1000, null=True)
    vehicle_accessory_price = models.CharField(max_length=100, null=True)
    vehicle_accessory_image = models.ImageField(upload_to='VehicleAccessories')
    store_id = models.ForeignKey(StoreDetailsModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.vehicle_accessory_name

    class Meta:
        db_table = 'vehicle_accessory_table'


# vehicle parts table
class VehiclePartsModel(models.Model):
    vehicle_id = models.ForeignKey(VehicleModel, on_delete=models.CASCADE)
    vehicle_part_id = models.AutoField(primary_key=True)
    vehicle_part_name = models.CharField(max_length=1000, null=True)
    vehicle_part_type = models.CharField(max_length=1000, null=True)
    vehicle_part_description = models.CharField(max_length=1000, null=True)
    vehicle_part_category = models.CharField(max_length=1000, null=True)
    vehicle_part_price = models.CharField(max_length=100, null=True)
    vehicle_part_image = models.ImageField(upload_to='VehicleParts')
    store_id = models.ForeignKey(StoreDetailsModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.vehicle_part_name

    class Meta:
        db_table = 'vehicle_parts_table'


class ServiceCategoryModel(models.Model):
    service_category_id = models.AutoField(primary_key=True)
    service_category_name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.service_category_name

    class Meta:
        db_table = 'service_Category_Table'


class ServiceModel(models.Model):
    service_id = models.AutoField(primary_key=True)
    store_id = models.ForeignKey(StoreDetailsModel, on_delete=models.CASCADE)
    service_category_id = models.ForeignKey(ServiceCategoryModel, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=1000, null=True)
    service_price = models.CharField(max_length=100, null=True)
    service_image = models.ImageField(upload_to='Store')

    def __str__(self):
        return self.service_type

    class Meta:
        db_table = 'Service_Table'


# vehicle image table
class VehicleImageModel(models.Model):
    vehicle_id = models.ForeignKey(VehicleModel, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to='Vehicle')

    class Meta:
        db_table = 'Vehicle_Images_Table'


class AccessoryImageModel(models.Model):
    image_id = models.AutoField(primary_key=True)
    accessory_image = models.ImageField(upload_to='VehicleAccessory')
    accessory_id = models.ForeignKey(VehicleAccessoryModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Accessory_Images_Table'


class PartsImageModel(models.Model):
    image_id = models.AutoField(primary_key=True)
    parts_image = models.ImageField(upload_to='VehicleParts')
    parts_id = models.ForeignKey(VehiclePartsModel, on_delete=models.CASCADE)


class BrandImageModel(models.Model):
    image_id = models.AutoField(primary_key=True)
    brand_name = models.ForeignKey(VehicleModel, on_delete=models.CASCADE)
    brand_image = models.ImageField(upload_to='Vehicle')

    def __str__(self):
        return self.brand_name

    class Meta:
        db_table = 'Brand_Images_Table'

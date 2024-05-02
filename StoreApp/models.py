from django.db import models

from AdminApp.models import *


# Create your models here.
class StoreDetailsModel(models.Model):
    store_id = models.AutoField(primary_key=True)
    store_name = models.CharField(max_length=1000, null=True)
    store_registration_id = models.CharField(max_length=100, null=True)
    store_image = models.ImageField(upload_to='Store/')
    store_phone = models.CharField(max_length=10)
    store_email = models.EmailField()
    store_date = models.DateField(auto_created=True)
    store_address = models.CharField(max_length=1000, null=True)
    store_district_id = models.ForeignKey(DistrictModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.store_name

    class Meta:
        db_table = 'Store_Details_Table'




# class StoreOfferModel(models.Model):
#     store_id = models.ForeignKey(StoreDetailsModel, on_delete=models.CASCADE)
#     store_location = models.ForeignKey(StoreLocationModel, on_delete=models.CASCADE)
#     store_offer_id = models.AutoField(primary_key=True)
#     store_offer_name = models.CharField(max_length=10)
#     store_offer_startdate = models.DateField()
#     store_offer_enddate = models.DateField()
#     store_offer_image = models.ImageField(upload_to='Store/', blank=True)
#
#     class Meta:
#         db_table = 'Store_Offer_Table'
#
# class StoreProductModel(models.Model):
#
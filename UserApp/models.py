from django.db import models
from AdminApp.models import *
from StoreApp.models import *
from VehicleApp.models import *


# Create your models here.
class UserModel(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=10)
    user_password = models.CharField(max_length=10)
    user_email = models.EmailField()
    user_phone = models.CharField(max_length=10)
    user_image = models.ImageField(upload_to='User/', null=True)
    user_status = models.BooleanField(default=True)
    user_created_at = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.user_name

    class Meta:
        db_table = 'user_table'


class UserAddressModel(models.Model):
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    user_address = models.CharField(max_length=500)
    user_address_id = models.AutoField(primary_key=True)
    user_district_id = models.ForeignKey(DistrictModel, on_delete=models.CASCADE)
    user_state_id = models.ForeignKey(StateModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_address

    class Meta:
        db_table = 'UserAddress_table'


# user service booking table
class UserBookingModel(models.Model):
    booking_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    user_address = models.ForeignKey(UserAddressModel, on_delete=models.CASCADE)
    store_id = models.ForeignKey(StoreDetailsModel, on_delete=models.CASCADE)
    service_id = models.ForeignKey(ServiceModel, on_delete=models.CASCADE)
    service_date = models.DateField()
    service_time = models.TimeField()

    class Meta:
        db_table = 'user_booking_table'


class UserReviewModel(models.Model):
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    store_id = models.ForeignKey(StoreDetailsModel, on_delete=models.CASCADE)
    booking_id = models.ForeignKey(UserBookingModel, on_delete=models.CASCADE)
    user_review = models.CharField(max_length=10)
    user_review_points = models.IntegerField()
    image_upload = models.ImageField(upload_to='Store')

    class Meta:
        db_table = 'user_review_table'

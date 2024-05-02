from django.db import models


# Create your models here.
class AdminModel(models.Model):
    admin_id = models.AutoField(primary_key=True)
    admin_name = models.CharField(max_length=10)
    admin_email = models.EmailField()
    admin_phone = models.CharField(max_length=10)
    admin_password = models.CharField(max_length=10)

    class Meta:
        db_table = 'admin_table'


class StateModel(models.Model):
    state_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.state_name

    class Meta:
        db_table = 'state_table'


class DistrictModel(models.Model):
    district_id = models.AutoField(primary_key=True)
    district_name = models.CharField(max_length=100, null=True)
    state_id = models.ForeignKey(StateModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.district_name

    class Meta:
        db_table = 'district_table'




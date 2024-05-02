from django.contrib import admin
from VehicleApp.models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(VehicleModel)
admin.site.register(VehicleAccessoryModel)
admin.site.register(VehiclePartsModel)
admin.site.register(ServiceCategoryModel)
admin.site.register(ServiceModel)
admin.site.register(VehicleImageModel)
admin.site.register(AccessoryImageModel)
admin.site.register(PartsImageModel)
admin.site.register(BrandImageModel)

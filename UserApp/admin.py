from django.contrib import admin
from UserApp.models import *

# Register your models here.
admin.site.register(UserModel)
admin.site.register(UserAddressModel)
admin.site.register(UserBookingModel)
admin.site.register(UserReviewModel)

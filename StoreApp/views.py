from django.shortcuts import render, redirect
from StoreApp.models import *
from AdminApp.models import *


# Create your views here.
def addstore(request):
    dist = DistrictModel.objects.all()
    if request.method == 'POST':
            store_name = request.POST.get('store_name')
            store_image = request.FILES['store_image']
            store_registration_id = request.POST.get('Registration_id')
            store_phone = request.POST.get('store_phone')
            store_email = request.POST.get('email')
            store_date = request.POST.get('Registration_date')
            store_address = request.POST.get('store_address')
            store_dist = DistrictModel.objects.get(district_id=request.POST.get('district'))

            new_store = StoreDetailsModel()
            new_store.store_name = store_name
            new_store.store_image = store_image
            new_store.store_registration_id = store_registration_id
            new_store.store_phone = store_phone
            new_store.store_email = store_email
            new_store.store_date = store_date
            new_store.store_address = store_address
            new_store.store_district_id = store_dist
            new_store.save()
            return redirect('/')
    return render(request, 'StoreRegistration.html', {'data': dist})





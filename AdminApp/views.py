from django.shortcuts import render, redirect
from VehicleApp.models import *
from UserApp.models import *
from StoreApp.models import *


# Create your views here.
def home(request):
    data = VehicleAccessoryModel.objects.all()
    datas = StoreDetailsModel.objects.all()
    pdata = VehiclePartsModel.objects.all()
    if request.method == 'POST':
        user_id = request.session['user']
        user = UserModel.objects.get(user_name=user_id)
        if user:
            return render(request, 'home.html', {'data': data, 'user': user, 'datas': datas, 'pdata': pdata})
        else:
            return redirect('/')
    return render(request, 'home.html', {'data': data, 'datas': datas, 'pdata': pdata})


def view(request, id):
    data = VehicleAccessoryModel.objects.filter(vehicle_accessory_id=id)
    datas = AccessoryImageModel.objects.filter(accessory_id=id)
    return render(request, 'productdetails.html', {'data': data, 'datas': datas})


def part_view(request, id):
    data = VehiclePartsModel.objects.filter(vehicle_part_id=id)
    datas = PartsImageModel.objects.filter(parts_id=id)
    return render(request, 'partsdetails.html', {'data': data, 'datas': datas})

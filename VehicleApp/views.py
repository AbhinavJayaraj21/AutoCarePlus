from django.shortcuts import render, HttpResponse,redirect
from django.shortcuts import get_object_or_404
from VehicleApp.models import *
from UserApp.models import *


# Create your views here.
def accessory(request):
    data = VehicleAccessoryModel.objects.all()
    pdata = VehiclePartsModel.objects.all()
    if request.method == 'POST':
        brand = request.POST.get('brand')
        model = request.POST.get('model')

    return render(request, 'bikeaccessory.html', {'data': data, 'pdata': pdata})


def buy_accessory(request, id):
    user_id = request.session['user']
    user = UserModel.objects.get(user_name=user_id)
    if user:
        data = get_object_or_404(VehicleAccessoryModel, vehicle_accessory_id=id)
        address = UserAddressModel.objects.get(user_id__user_name=user_id)
        print(address)
        return render(request, 'accessory_buy.html', {'data': [data], 'address': [address]})
    else:
        return redirect('login/')

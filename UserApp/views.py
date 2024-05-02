from django.shortcuts import render, HttpResponse, redirect
from UserApp.models import *


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('pswd')
        user = UserModel.objects.filter(user_name=username, user_password=password)
        if user:
            request.session['user'] = username
            return redirect('/')
        else:
            return redirect('/login')
    return render(request, 'login.html')


def logout(request):
    print("logout fun called")
    del request.session['user']
    return redirect('/')


def profile(request):
    user_id = request.session['user']
    user = UserModel.objects.get(user_name=user_id)
    user_address = UserAddressModel.objects.get(user_id=user.user_id)
    print(user_address)
    return render(request, 'userprofile.html', {'user': [user], 'datas': [user_address]})


def update_profile(request, id):
    data = UserModel.objects.filter(user_id=id)
    if request.method == 'POST':
        user_id = request.session['user']



# datas = BookModel.objects.filter(id=id)
#     if request.method == 'POST':
#         d1 = BookModel.objects.get(id=id)
#         d1.title = request.POST.get('title')
#         d1.description = request.POST.get('desc')
#         d1.price = request.POST.get('price')
#         d1.save()
#         return redirect('/')
#     return render(request, 'update.html', {'data': datas})

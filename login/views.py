from multiprocessing import context
from webbrowser import get
from django.shortcuts import render, get_object_or_404
from register_user.models import Nguoidung
# Create your views here.
def login(request):
    return render(request,'login.html')

def login_process(request):
    username = request.GET.get('username')
    password = request.GET.get('password')
    
    data = Nguoidung.objects.filter(username = username, password = password)
    danhsach = Nguoidung.objects.all()
    context= {
        'ds_nguoidung': danhsach,
    }
    if data.exists():
        return render (request, 'list.html', context)
    else:
        return render (request, 'login_fail.html')
def detail(request,username_id):
    user = get_object_or_404(Nguoidung, pk = username_id)
    context =  {
        'user' : user
    }
    return render(request,'detail.html', context)
def update_process(request):
    id = request.GET.get('id')
    username = request.GET.get('username')
    email = request.GET.get('email')
    password = request.GET.get('password')
    Nguoidung.objects.filter(id = id).update(
        username = username,
        email = email,
        password = password,
    )
    # data = Nguoidung.objects.filter(username = username, password = password)
    list = Nguoidung.objects.all()
    context = {
        'ds_nguoidung' : list,
    }
    return render (request,'list.html', context)

def delete_user(request, username_id):
    data = get_object_or_404(Nguoidung, pk = username_id)
    try:
        data.delete()
    except:
        print("Delete error!")

    list = Nguoidung.objects.all()
    context = {
        'ds_nguoidung' : list,
    }
    return render (request,'list.html', context)


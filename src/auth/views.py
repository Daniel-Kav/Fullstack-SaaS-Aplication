from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username= username, password= password)


        if request.user :
            login(request, user)
            print ("Login successful")
            return redirect("/")
    return render(request,'auth/login.html',{})

def register_user(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username= username, password=password)

        if request.user:
            user.save()
            login(request, user)
            return redirect("/")
    return render(request,'auth/register.html',{})

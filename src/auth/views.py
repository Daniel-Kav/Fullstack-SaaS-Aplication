from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate

# Create your views here.
def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(username= username, password= password)


    if request.user is not None:
        login(request, user)
        print ("Login successful")
        redirect("/")
    return render(request,'auth/login.html',{})
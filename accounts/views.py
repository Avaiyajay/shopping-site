from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
import random
import math

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        pass1 = request.POST["password"]

        user = auth.authenticate(username=username,password = pass1)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Enter Valid Username or password")
            return redirect('login')

    return render(request,"loginform.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        pass1 = request.POST["password1"]
        pass2 = request.POST["password2"]

        if pass1 == pass2:
            if(len(pass1) < 4):
                messages.info(request,"Password is too short")
                return redirect('signup')
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username is already taken")
                return redirect('signup')
            if User.objects.filter(email = email).exists():
                messages.info(request,"Email must be unique")
                return redirect('signup')
            user = User.objects.create_user(username=username,email=email,password=pass1)
            user.save()
            return redirect('login')
        else:
            messages.info(request,"Password didn't match")
            return redirect('signup')
    return render(request,'signup.html')


def forgotPassword(request):
    pass
    # digits = [i for i in range(0, 10)]
    # random_str = ""
    # for i in range(6):
    #     index = math.floor(random.random() * 10)
    #     random_str += str(digits[index])
    # if request.method == "POST":
    #     email = request.POST['email']
    #     user = User.objects.filter(email = email)
    #     if(user):
    #         return
    #     else:
    #         messages.info(request,"There is no account exist with this email,enter email when you create account")
    #         return redirect('forgot_password')
    #
    # return render(request,"forgot_password.html")


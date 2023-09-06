

from django.contrib.auth.hashers import make_password
from django.db import connection
from django.contrib.auth import get_user_model ,login as auth_login
from django.shortcuts import redirect, render
from django.contrib import messages 

from .forms import UserLoginForm

def login(request):
    """
        This is a unsecure way of login 
        you should make it secure according to what have been told in 
        topic 1 : sqli             
        Intentional vulnerability (DO NOT USE IN REAL WORLD CODE)
    """
    if(request.method=="POST"):
        form=UserLoginForm(data=request.POST)
        if(form.is_valid()):
            cd=form.cleaned_data
            username=cd["username"]
            password=make_password(cd['password'])
            users = f"SELECT * FROM auth_user WHERE username = '{username}' AND password = '{password}'"
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM auth_user;")
                result=cursor.fetchone()
            if(result):
                user=get_user_model().objects.get(id=result[0])
                if(user.is_active):
                    auth_login(request, user)
                    return(redirect('/'))
                else:
                    messages.error(request,"حساب کاربری شما غیر فعال است.لطفا به ایمیل خود رفته با ایمیل ارسال شده حساب خود را فعال کنید.")
            else:
                messages.error(request,"نام کاربری یا رمز عبور وارد شده صحیح نمی باشد.")
    return(render(request,"auth/login.html")) 
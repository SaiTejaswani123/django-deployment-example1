from django.shortcuts import render
from AppTwo.models import User

def index(request):
    return render(request,"AppTwo/myfirst.html")


def users(request):
    user_list=User.objects.order_by("first_name")
    userinterface={"action":user_list}
    return render(request,"AppTwo/users.html",context=userinterface)

from django.shortcuts import render
from cantact_app.models import accuntmodel

# Create your views here.

def home(request):
     # profilestatus = 'کاربر معمولی'
    if request.user.is_authenticated:
        us = accuntmodel.objects.all()
        for u in us:
            if u.melicode == request.user.username:
                profilestatus = f"{u.level} {u.firstname} {u.lastname}"
    else:
        profilestatus = 'ورود به کاربری'

    return render(request,'home.html',context={
                                                'profilestatus':profilestatus,
    })

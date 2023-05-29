from django.shortcuts import render
from cantact_app.models import accuntmodel

# Create your views here.
profilestatus =['']
def home(request):
    if request.user.is_authenticated:
        us = accuntmodel.objects.all()
        for u in us:
            if u.melicode == request.user.username:
                profilestatus[0] = f"{u.firstname} {u.lastname} عزیز خوش آمدید "
    else:
        profilestatus[0] = 'ورود به کاربری'

    return render(request,'home.html',context={
                                                'profilestatus':profilestatus[0],
    })

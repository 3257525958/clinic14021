from django.shortcuts import render
from jobs_app.models import workmodel
ww = ['t']
def reservdef(request):
    works = workmodel.objects.all()
    ww.clear()
    for w in works :
        ww.append(w)

    return render(request,'reserv.html',context={'works':works,

    })
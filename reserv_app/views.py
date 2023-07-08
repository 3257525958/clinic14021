from django.shortcuts import render
from jobs_app.models import workmodel

def reservdef(request):
    works = workmodel.objects.all()
    for w in works :
      print(w.work)
    return render(request,'reserv.html',context={'works':works,

    })
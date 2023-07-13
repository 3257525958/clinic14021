from django.shortcuts import render
from jobs_app.models import workmodel
ww = ['t']
def reservdef(request):
    works = workmodel.objects.all()
    ww.clear()
    ww.append('start')
    for w in works :
        a = 0
        for x in ww :
            if x ==  w.work :
                a = 1
        if a == 0 :
            ww.append(w.work)
    ww.pop(0)
    return render(request,'reserv.html',context={'works':works,
                                                 'job':ww,
                                                 })
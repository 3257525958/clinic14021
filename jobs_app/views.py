from django.shortcuts import render
from jobs_app.models import jobsmodel

newjob_etebar = ['true']

def jobs(request):
    savejob = request.POST.get("savejob")
    newjob = request.POST.get("newjob")
    print(newjob)
    print(newjob_etebar[0])
    print(savejob)
    if savejob == 'accept':
        print("1")
        newjob_etebar[0] = "true"
        if (newjob == '') or (newjob == None):
            print("2")
            newjob_etebar[0] = "false"
        else:
            print("3")
            jobsmodel.objects.create(job=newjob)
            newjob_etebar[0] = "ok"

    return render(request,"jobs.html",context={'newjob_etebar':newjob_etebar[0]})

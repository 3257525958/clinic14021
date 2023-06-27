from django.shortcuts import render
from jobs_app.models import jobsmodel , employeemodel
from cantact_app.models import accuntmodel

newjob_etebar = ['true']
delet_etebar = ['true']
employee_etebar = ['true']
jobemployee = ['true']
jobemployee[0] = 'true'
useretebar = ['true']
message = ['true']
def jobs(request):
    savejob = request.POST.get("savejob")
    newjob = request.POST.get("newjob")
    newemployee = request.POST.get("newemployee")
    deletjob = request.POST.get("deletjob")
    buttondeletjob = request.POST.get("buttondeletjob")
    addbuttonemployee =request.POST.get("addbuttonemployee")
    employeeforjob = request.POST.get("employeeforjob")
    melicode = request.POST.get("melicode")
# ****************************************************اضافه کردن یک فعالیت********************************************************
    newjob_etebar[0] = 'true'
    if savejob == 'accept':
        newjob_etebar[0] = "true"
        if (newjob == '') or (newjob == None):
            newjob_etebar[0] = "false"
        else:
            js = jobsmodel.objects.all()
            a = 0
            for j in js :
                if j.job == newjob:
                    a = 1
                    newjob_etebar[0] = "repeat"
                    break
            if a == 0 :
                jobsmodel.objects.create(job=newjob,employee=newemployee)
                newjob_etebar[0] = "ok"
# ******************************************************************حذف کردن یک فعالیت******************************************************
    delet_etebar[0] = 'true'
    js = jobsmodel.objects.all()
    lenj = len(js)
    if buttondeletjob == 'accept' :
        delet_etebar[0] ='ok'
        if (deletjob != '') and (deletjob != None) :
            c = 0
            js = jobsmodel.objects.all()
            for j in js :
                if c == int(deletjob) :
                    delet_etebar[0] = 'delet'
                    a = jobsmodel.objects.filter(job=j.job)
                    a.delete()
                c += 1
# ***************************************************************تعریف دسترسی برای هر کدوم از نیروها ******************************************************
    employee_etebar[0] = 't'
    useretebar[0] = 'f'

    users = accuntmodel.objects.all()
    for user in users :
        if user.melicode == melicode :
            useretebar[0] = 'true'
            break
        else:
            useretebar[0] = 'false'

    js = jobsmodel.objects.all()
    jobemployee.clear()
    for j in js :
        jobemployee.append(j.employee)

    lenj = len(js)

    if addbuttonemployee == 'accept' :
        employee_etebar[0] = 'ok'
        if (employeeforjob != '') and (employeeforjob != None)  :
            if useretebar[0] == 'true':
                c = 0
                js = jobsmodel.objects.all()
                for j in js:
                    if c == int(employeeforjob):
                        employeemodel.objects.create(employee=j.employee, melicod=melicode)
                        users = accuntmodel.objects.all()
                        employee_etebar[0] = 'addmployee'
                        for user in users :
                            if user.melicode == melicode :
                                message[0] = f"{j.employee} برای {user.firstname} {user.lastname} "
                                break
                        break
                    c += 1




# *****************************************************************************************************************
    js = jobsmodel.objects.all()
    return render(request,"jobs.html",context={'newjob_etebar':newjob_etebar[0],
                                               'delet_etebar':delet_etebar[0],
                                               'actcount':lenj,
                                               'jobs': js ,
                                               'jobemployee':jobemployee,
                                               'useretebar':useretebar[0],
                                               'employeeetebar':employee_etebar[0],
                                               'employeemessage':message[0]
                                               })

from django.shortcuts import render
from jobs_app.models import jobsmodel , employeemodel
from cantact_app.models import accuntmodel
from store_app.models import storemodel

newjob_etebar = ['true']
newemploy_etebar = ['true']
delet_etebar = ['true']
employee_etebar = ['true']
jobemployee = ['true']
jobemployee[0] = 'true'
useretebar = ['true']
message = ['true']
deletemploy_etebar = ['t']
employerjoblist = ['t']
melicodearay = ['']
joblist = ['t']
joblistforjava = ['t']
emplist = ['انتخاب کنید']
selectjob = ['t']
def jobs(request):
    savejob = request.POST.get("savejob")
    newjob = request.POST.get("newjob")
    newemployee = request.POST.get("newemployee")
    deletjob = request.POST.get("deletjob")
    buttondeletjob = request.POST.get("buttondeletjob")
    addbuttonemployee =request.POST.get("addbuttonemployee")
    employeeforjob = request.POST.get("employeeforjob")
    melicode = request.POST.get("melicode")
    deletemploy = request.POST.get("deletemploy")
    employmelicode = request.POST.get("employmelicode")
    empnumber = request.POST.get("empnumber")
    cearshmelicode = request.POST.get("cearshmelicode")
    facebutton = request.POST.get("facebutton")
    servicselector = request.POST.get("servicselector")
# ****************************************************اضافه کردن یک فعالیت********************************************************
    newjob_etebar[0] = 'true'
    newemploy_etebar[0] = 'true'
    if savejob == 'accept':
        newjob_etebar[0] = "true"
        if (newjob == '') or (newjob == None):
            newjob_etebar[0] = "false"
        else:
            if (newemployee == '') or (newemployee == None):
                newemploy_etebar[0] = 'false'
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


    js = jobsmodel.objects.all()
    jobemployee.clear()
    for j in js :
        jobemployee.append(j.employee)

    lenj = len(js)

    if addbuttonemployee == 'accept' :
        if (melicode != '') and (melicode != None):
            users = accuntmodel.objects.all()
            for user in users:
                if user.melicode == melicode:
                    useretebar[0] = 'true'
                    break
                else:
                    useretebar[0] = 'false'
        else:
            useretebar[0] = 'empty'
        if (employeeforjob != '') and (employeeforjob != None)  :
            employee_etebar[0] = 'None'
            if useretebar[0] == 'true':
                c = 0
                js = jobsmodel.objects.all()
                for j in js:
                    if c == int(employeeforjob):
                        employees = employeemodel.objects.all()
                        for emp in employees :
                            if emp.melicod == melicode :
                                if emp.employee == j.employee :
                                    employee_etebar[0] = "repeat"
                                    message[0] = f" شغل {j.employee} برای {user.firstname} {user.lastname} "
                        if employee_etebar[0] != "repeat" :
                            employeemodel.objects.create(employee=j.employee, melicod=melicode)
                            users = accuntmodel.objects.all()
                            employee_etebar[0] = 'addmployee'
                            for user in users :
                                if user.melicode == melicode :
                                    message[0] = f" شغل {j.employee} برای {user.firstname} {user.lastname} "
                                    break
                            break
                    c += 1
        else:
            employee_etebar[0] = 'ok'

# ****************************************************************حدف یک شغل برای یک کارمند*************************************************
    employename = ''
    deletemploy_etebar[0] = 't'
    employerjoblist.clear()
    employs = employeemodel.objects.all()
    for emp in employs :
        if emp.melicod == employmelicode :
            employerjoblist.append(emp.employee)
    lenemploy = len(employerjoblist)

    if cearshmelicode == 'accept' :
        # employmelicode = melicodearay[0]
        if (employmelicode !='') and (employmelicode != None) :
            employs = employeemodel.objects.all()
            for emp in employs :
                if int(emp.melicod) == int(employmelicode) :
                    deletemploy_etebar[0] = 'true'
                    melicodearay[0] = employmelicode
                    users = accuntmodel.objects.all()
                    for user in users :
                        if user.melicode == employmelicode :
                            employename = user.firstname +' '+user.lastname
                    break
                else:
                    deletemploy_etebar[0] = "false"
                    melicodearay[0] = ''
        else:
            deletemploy_etebar[0] = "empty"

    if deletemploy == "accept":
        if (empnumber != '') and (empnumber != None):
            employmelicode = melicodearay[0]
            employerjoblist.clear()
            employs = employeemodel.objects.all()
            for emp in employs:
                if emp.melicod == employmelicode:
                    employerjoblist.append(emp.employee)
            lenemploy = len(employerjoblist)
            a = employeemodel.objects.filter(melicod=employmelicode, employee=employerjoblist[int(empnumber)])
            a.delete()
            deletemploy_etebar[0] = 'delet'
            melicodearay[0] = ''
        else:
            deletemploy_etebar[0] = 'emptyjob'
            melicodearay[0] = ''
# **********************************************************ساختن یک خدمت*********************************************************
    selectjob[0] = "t"
    servicselect = "انتخاب کنیدددد"
    joblist.clear()
    allservic = jobsmodel.objects.all()
    for ser in allservic :
        joblist.append(ser.job)

    if facebutton == "accept" :
        print("1")
        selectjob[0] = 'true'
        servicselect = joblist[int(servicselector)]
        allservic = jobsmodel.objects.all()
        for ser in allservic :
            print(ser.job)
            print(joblist[int(servicselector)])
            if ser.job == joblist[int(servicselector)] :
                print("2")
                emps = employeemodel.objects.all()
                for emp in emps :
                    print(ser.employee)
                    print(emp.employee)
                    if ser.employee == emp.employee :
                        print("3")
                        users = accuntmodel.objects.all()
                        for user in users :
                            print(emp.melicod)
                            print(user.melicode)
                            if emp.melicod == user.melicode :
                                print("4")
                                emplist.append(user.firstname+' '+user.lastname)
                                print(emplist)


# ****************************************************************************************************************************************
    js = jobsmodel.objects.all()
    return render(request,"jobs.html",context={'newjob_etebar':newjob_etebar[0],
                                               'newemploy_etebar':newemploy_etebar[0],
                                               'delet_etebar':delet_etebar[0],
                                               'actcount':lenj,
                                               'jobs': js ,
                                               'jobemployee':jobemployee,
                                               'useretebar':useretebar[0],
                                               'employeeetebar':employee_etebar[0],
                                               'employeemessage':message[0],
                                               'deletemployetebar':deletemploy_etebar[0],
                                               'lenemploy':lenemploy,
                                               'employerjoblist':employerjoblist,
                                               'employename':employename,
                                               'allservic':joblist,
                                               'allemployee':emplist,
                                               'servicselect':servicselect,
                                               'selectjob':selectjob[0],
                                               'emplist':emplist,
                                               })

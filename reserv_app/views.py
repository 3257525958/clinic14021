from django.shortcuts import render, redirect
from jobs_app.models import workmodel
import datetime
from jalali_date import date2jalali,datetime2jalali
from datetime import timedelta
import matplotlib
from reserv_app.models import reservemodel
from cantact_app.models import accuntmodel
matplotlib.use('Agg')
def strb(tdef):
    x = str(datetime2jalali(tdef).strftime('%a %d %b %y'))
    rmonth = x[7:10]
    ag_month = rmonth
    if ag_month == 'Far':
        ag_month = 'فروردین'
    if ag_month == 'Ord':
        ag_month = 'اردیبهشت'
    if ag_month == 'Kho':
        ag_month = 'خرداد'
    if ag_month == 'Tir':
        ag_month = 'تیر'
    if ag_month == 'Mor':
        ag_month = 'مرداد'
    if ag_month == 'Sha':
        ag_month = 'شهریور'
    if ag_month == 'Meh':
        ag_month = 'مهر'
    if ag_month == 'Aba':
        ag_month = 'آبان'
    if ag_month == 'Aza':
        ag_month = 'آذر'
    if ag_month == 'Dey':
        ag_month = 'دی'
    if ag_month == 'Bah':
        ag_month = 'بهمن'
    if ag_month == 'Esf':
        ag_month = 'اسفند'
    rmonth = ag_month
    return (rmonth)
def strd(tdef):
    x = str(datetime2jalali(tdef).strftime('%a %d %b %y'))
    rday = x[4:6]
    if rday == '01':
        rday = '1'
    if rday == '02':
        rday = '2'
    if rday == '03':
        rday = '3'
    if rday == '04':
        rday = '4'
    if rday == '05':
        rday = '5'
    if rday == '06':
        rday = '6'
    if rday == '07':
        rday = '7'
    if rday == '08':
        rday = '8'
    if rday == '09':
        rday = '9'
    return (rday)
def stra(tdef):
    x = str(datetime2jalali(tdef).strftime('%a %d %b %y'))
    rweek = x[0:3]
    if rweek == 'Sat':
        rweek = 'شنبه'
    if rweek == 'Sun':
        rweek = 'یکشنبه'
    if rweek == 'Mon':
        rweek = 'دوشنبه'
    if rweek == 'Tue':
        rweek = 'سه‌شنبه'
    if rweek == 'Wed':
        rweek = 'چهارشنبه'
    if rweek == 'Thu':
        rweek = 'پنج‌شنبه'
    if rweek == 'Fri':
        rweek = 'جمعه'
    return (rweek)
def stry(tdef):
    x = str(datetime2jalali(tdef).strftime('%a %d %b %y'))
    ryear = x[11:]
    return (ryear)
def stradb(tdef):
    r = stra(tdef)+' '+strd(tdef)+' '+strb(tdef)
    return (r)

ww = ['t']
shamsiarray = ['t']
miladiarray = ['t']
selectprocedure = ['t']
reservetebar = ['t']
day = ['t']
day.clear()
level = ['']
loginetebar = ['t']

def reservdef(request):
    if request.user.is_authenticated:
        users = accuntmodel.objects.all()
        for user in users:
            if user.melicode == request.user.username:
                level[0] = user.level
                print(level[0])
        inputwork = request.POST.get("inputwork")
        timeselect = request.POST.get("timeselect")
    # *******************************************************ساختن آرایه ها برای نمایش خدمتها در صفحه وب********************************************
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
    #**********************انتخاب کاربر به صورت یک عدد از forloop  از وب میاد و در اینجا اون عدد تبدیل میشه به انتخاب اصلی و در  f  ریخته میشه**************
        c = 0
        if inputwork != None:
            for f in works :
                if int(c) == int(inputwork) :
                    selectprocedure.clear()
                    selectprocedure.append(f.work)
                    selectprocedure.append(f.detalework)
                    selectprocedure.append(f.person)

                    if f.time == "نیم ساعت" :
                        selectprocedure.append("1")
                    if f.time == "یک ساعت" :
                        selectprocedure.append("2")
                    if f.time =="یک و نیم ساعت" :
                        selectprocedure.append("3")
                    if f.time == "دو ساعت" :
                        selectprocedure.append("4")
                    if f.time == "دو نیم ساعت" :
                        selectprocedure.append("5")
                    selectprocedure.append(f.cast)
                    # reservemodel.objects.create(jobreserv=selectprocedure[0],
                    #                             detalereserv=selectprocedure[1],
                    #                             personreserv=selectprocedure[2],
                    #                             timereserv=selectprocedure[3],
                    #                             castreserv=selectprocedure[4],
                    #                             dateshamsireserv=selectprocedure[5],
                    #                             datemiladireserv=selectprocedure[6],
                    #                             yearshamsi=selectprocedure[7],
                    #                             hourreserv=selectprocedure[8],
                    #                             )
                c +=1

            shamsiarray.clear()
            miladiarray.clear()
            day.clear()
            reservs = reservemodel.objects.all()

            t = datetime.datetime.now()
            mount = strb(t)
            tedaderooz = 0
            if int(strd(t)) >= 20 :
                for i in range(30) :
                    if strb(t) != mount :
                        break
                    tedaderooz += 1
                    t += timedelta(days=1)
            t = datetime.datetime.now()
            if int(strd(t)) < 20 :
                tedaderooz = 30
            t = datetime.datetime.now()
            for i in range(tedaderooz) :
                shamsiarray.append(stradb(t))
                miladiarray.append(t.strftime('%a %d %b %y'))
                dayarr = ['t']
                dayarr.clear()
                dayarr.append(stradb(t))
                for h in range(20):
                    dayarr.append('true')
                for r in reservs :
                    if r.personreserv == selectprocedure[2] :
                        if r.dateshamsireserv == stradb(t) :
                            dayarr[int(r.hourreserv)] = "false"
                t += timedelta(days=1)
                day.append(dayarr)
            return render(request,'timereserv.html',context={'day':day,
                                                             })

        if (timeselect != None) and (timeselect != '') :
            s = timeselect
            stime = s.split(",")
            selectprocedure.append(shamsiarray[int(stime[1])-1])
            selectprocedure.append(miladiarray[int(stime[1])-1])
            selectprocedure.append(stry(datetime.datetime.now()))
            selectprocedure.append(stime[0])

            reservs = reservemodel.objects.all()
            reservetebar[0] = 'succes'
            if selectprocedure[3] == "1" :
                reservetebar[0] = "succes"
            t = 0
            if selectprocedure[3] == '2' :
                t = int(selectprocedure[8])
                for r in reservs :
                    if r.personreserv == selectprocedure[2] :
                        if r.dateshamsireserv == selectprocedure[5] :
                            if int(r.timereserv) == int(t) +1:
                                reservetebar[0] = "false2"
            if selectprocedure[3] == '3' :
                t = int(selectprocedure[8])
                for r in reservs :
                    if r.personreserv == selectprocedure[2] :
                        if r.dateshamsireserv == selectprocedure[5] :
                            if int(r.timereserv) == int(t) +1:
                                reservetebar[0] = "fals3"
                            if int(r.timereserv) == int(t) + 2:
                                reservetebar[0] = "false3"

            if selectprocedure[3] == '4' :
                t = int(selectprocedure[8])
                for r in reservs :
                    if r.personreserv == selectprocedure[2] :
                        if r.dateshamsireserv == selectprocedure[5] :
                            if int(r.timereserv) == int(t) + 1:
                                reservetebar[0] = "false4"
                            if int(r.timereserv) == int(t) + 2:
                                reservetebar[0] = "false4"
                            if int(r.timereserv) == int(t) + 3:
                                reservetebar[0] = "false4"

            if selectprocedure[3] == '5' :
                t = int(selectprocedure[8])
                for r in reservs :
                    if r.personreserv == selectprocedure[2] :
                        if r.dateshamsireserv == selectprocedure[5] :
                            if int(r.timereserv) == int(t) + 1:
                                reservetebar[0] = "false5"
                            if int(r.timereserv) == int(t) + 2:
                                reservetebar[0] = "false5"
                            if int(r.timereserv) == int(t) + 3:
                                reservetebar[0] = "false5"
                            if int(r.timereserv) == int(t) + 4:
                                reservetebar[0] = "false5"

            if reservetebar[0] == 'succes' :
                reservemodel.objects.create(jobreserv=selectprocedure[0],
                                            detalereserv=selectprocedure[1],
                                            personreserv=selectprocedure[2],
                                            timereserv=selectprocedure[3],
                                            castreserv=selectprocedure[4],
                                            dateshamsireserv=selectprocedure[5],
                                            datemiladireserv=selectprocedure[6],
                                            yearshamsi=selectprocedure[7],
                                            hourreserv=selectprocedure[8],
                                            )
                return render(request,'reserv_end.html')
            else:
                return render(request,'timereserv.html',context={'reservetebar':reservetebar[0],})
        return render(request,'reserv.html',context={'works':works,
                                                 'job':ww,
                                                 'shamsiarray':shamsiarray,
                                                 })
    else:
        loginetebar[0] = "false"
        return render(request,'home.html',context={"loginetebar":loginetebar[0]})
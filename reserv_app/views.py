from django.shortcuts import render
from jobs_app.models import workmodel
import datetime
from jalali_date import date2jalali,datetime2jalali
from datetime import timedelta
import matplotlib
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
def reservdef(request):
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
                print(f.work,f.detalework,f.person,f.time,f.cast)
                # reservemodel.objects.create(jobreserv=f.work,
                #                             detalereserv=f.detalework,
                #                             personreserv=f.person,
                #                             timereserv=f.time,
                #                             castreserv=f.cast,
                #                             dateshamsireserv=,
                #                             datemiladireserv=,
                #                             yearshamsi=,
                #                             )
        c +=1

        print(stradb(datetime.datetime.now()))
        print(stry(datetime.datetime.now()))
        print(datetime.datetime.now().strftime('%a %d %b %y'))
        shamsiarray.clear()
        miladiarray.clear()
        t = datetime.datetime.now()
        for i in range(30) :
            shamsiarray.append(stradb(t))
            miladiarray.append(t.strftime('%a %d %b %y'))
            t += timedelta(days=1)
        print(shamsiarray)
        print(miladiarray)
        if timeselect != None :
            s = timeselect
        else:
            s = "qqqqqqqqq,wwwwwwwwww"
        sp = s.split(",")
        print(sp[0],sp[1])
        print(timeselect)
        return render(request,'timereserv.html',context={'shamsiarray':shamsiarray,
                                                         })
    return render(request,'reserv.html',context={'works':works,
                                                 'job':ww,
                                                 'shamsiarray':shamsiarray,
                                                 })
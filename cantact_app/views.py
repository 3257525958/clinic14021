from django.shortcuts import render , redirect
import tkinter
from tkinter import messagebox
import datetime
from jalali_date import date2jalali,datetime2jalali
from datetime import timedelta
from cantact_app.models import accuntmodel
from cantact_app.forms import accuntform
# Create your views here.
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
def stradby(tdef):
    r = stra(tdef)+' '+strd(tdef)+' '+strb(tdef)+' '+stry(tdef)
    return (r)
def stryabd(tdef):
    r = stry(tdef)+' '+stra(tdef)+' '+strb(tdef)+' '+strd(tdef)
    return (r)
def stryadb(tdef):
    r = stry(tdef)+' '+stra(tdef)+' '+strd(tdef)+' '+strb(tdef)
    return (r)
def strn():
    tx = datetime.datetime.now()
    r = stry(tx)+' '+stra(tx)+' '+strd(tx)+' '+strb(tx)
    return (r)
def strbd(tdef):
    r = strb(tdef)+' '+strd(tdef)
    return (r)

t = [datetime.datetime.now()]
t[0] = datetime.datetime.now()
year = [int(str('14' + stry(datetime.datetime.now())))]
year[0] =int(str('14' + stry(datetime.datetime.now())))
calandar_array_for_show = ['0']
calandar_array_for_show[0] ='0'
calandar_array_for_miladidate = [datetime.datetime.now()]
calandar_array_for_miladidate[0] = datetime.datetime.now()
calandar_array_for_shamsidate = [stradby(t[0])]
calandar_array_for_shamsidate [0] = stradby(t[0])
firstname_r = ['']
lastname_r = ['']
melicod_r = ['']
phonnumber_r = ['']
berthmiladi_r = [datetime.datetime.now()]
berthmiladi_r[0] = datetime.datetime.now()
def addcantactdef(request):
    bbtn = request.POST.get("bbtn")
    input_year = request.POST.get("input_year")
    if (input_year == None) or (input_year == ''):
        input_year = str(year[0])
    button_upmounth = request.POST.get("button_upmounth")
    button_downmounth = request.POST.get("button_downmounth")
    button_calandar = request.POST.get("button_calandar")
    button_back = request.POST.get("button_back")
    button_send = request.POST.get('button_send')
    formuser = accuntform(request.POST, request.FILES)
# ---------اگر دکمه تقئیم خورد سال رو به هم اکنون تغییر میده دقت شود که در مواد دیگه مثل بالا زدن-سال یا چیزی دیگه - button calandar برابر acceot میشد-----------------------------------متوجه شدم که placeholder-مقدارش داخل input خواهد بود----------------------------------------------------------------
    if button_calandar == "accept" :
        year[0] = int(str('14' + stry(datetime.datetime.now())))
        input_year = year[0]
        t[0] = datetime.datetime.now()
        calandar_array_for_show[0] = '0'
        calandar_array_for_miladidate[0] = datetime.datetime.now()
        calandar_array_for_shamsidate[0] = stradby(t[0])
        berthmiladi_r[0] = datetime.datetime.now()
    # ---------- در این قسمت داده هایی که به صفحه addcontact داده میشود در آرایه هایدمربوطه ذخیره میشه تا با زدن دکمه ها اونا نپرن ----
    firstname = request.POST.get("firstname")
    if (firstname != '') and ( firstname != None) :
        firstname_r[0] = firstname
    if firstname_r[0] == None :
        firstname_r[0] = ''

    lastname = request.POST.get("lastname")
    if (lastname != '') and ( lastname != None) :
        lastname_r[0] = lastname
    if lastname_r[0] == None :
        lastname_r[0] = ''

    melicod = request.POST.get("melicod")
    if (melicod != '') and ( melicod != None) :
        melicod_r[0] = melicod
    if melicod_r[0] == None :
        melicod_r[0] = ''

    phonnumber = request.POST.get("phonnumber")
    if (phonnumber != '') and ( phonnumber != None) :
        phonnumber_r[0] = phonnumber
    if phonnumber_r[0] == None :
        phonnumber_r[0] = ''
# ****************************************************کلید برگشت**********************************************
    if button_back == "accept" :
        return redirect('/')
# -----------------------------------------------------------------انتخاب روز تولد----------------------------------------------
    if (bbtn != None) and (bbtn != '') and (calandar_array_for_show != None) and (calandar_array_for_show != '') :
        berthmiladi_r[0] = calandar_array_for_miladidate[int(bbtn)]
        return render(request,'add_cantact.html',context={ "firstname":firstname_r[0],
                                                           "lastname":lastname_r[0],
                                                           "melicod":melicod_r[0],
                                                           "phonnumber":phonnumber_r[0],
                                                           "year" : year[0],
                                                           "berthday_shamsi":calandar_array_for_shamsidate[int(bbtn)],
                                                          })
# ---------------------------------------------------------------------------------
    if(input_year != None) and (input_year != ''):
        if int(input_year) < 1200:
            input_year = 1402
        if int(input_year) > int(str('14' + stry(datetime.datetime.now()))):
            input_year = str(year[0])
        mounth_of_t = strb(t[0])
        while int(input_year) != year[0] :
            if int(input_year) < year[0] :
                if (strb(t[0]) == 'فروردین') and (strd(t[0]) == '1'):
                    year[0] -= 1
                    button_calandar = "accept"
                    button_upmounth = None
                    button_downmounth = None
                t[0] -= timedelta(days=1)
            if int(input_year) > year[0] :
                if (strb(t[0]) == 'فروردین') and (strd(t[0]) == '1'):
                    year[0] += 1
                    button_calandar = "accept"
                    button_upmounth = None
                    button_downmounth = None
                t[0] += timedelta(days=1)

        if strb(t[0]) == 'اسفند' :
            while strb(t[0]) != mounth_of_t :
                t[0] -= timedelta(days=1)
        if strb(t[0]) == 'فروردین' :
            while strb(t[0]) != mounth_of_t :
                t[0] += timedelta(days=1)
# ----------------------------------------------------------------------------------------------------------
    if button_upmounth == "accept" :
        button_calandar = "accept"
        mounth = strb(t[0])
        while strb(t[0]) == mounth :
            t[0] += timedelta(days=1)
        if strb(t[0]) == 'فروردین' :
            year[0] += 1
# -----------------------------------------------------------------------------------------------------
    if button_downmounth == "accept" :
        button_calandar = "accept"
        mounth = strb(t[0])
        while strb(t[0]) == mounth :
            t[0] -= timedelta(days=1)
        if strb(t[0]) == 'اسفند' :
            year[0] -= 1
# ------------------------------------------------------------------------------------------------------
    if button_calandar == "accept" :
        mounth = strb(t[0])
        day_of_mounth = strd(t[0])
        day_of_week = stra(t[0])
        r = 0
        g = 0
        calandar_array_for_show.clear()
        calandar_array_for_miladidate.clear()
        calandar_array_for_shamsidate.clear()

        for r in range(int(day_of_mounth)) :
            t[0] -= timedelta(days=1)
        while stra(t[0]) != 'جمعه' :
            t[0] -= timedelta(days=1)
            calandar_array_for_show.append('')
            calandar_array_for_miladidate.append(t[0])
            calandar_array_for_shamsidate.append(stradby(t[0]))

        calandar_array_for_show.append('')
        calandar_array_for_miladidate.append(t[0])
        calandar_array_for_shamsidate.append(stradby(t[0]))
        while strd(t[0]) != "1" :
            t[0] +=timedelta(days=1)
        i = 0
        while strb(t[0]) == mounth :
            i += 1
            calandar_array_for_show.append(i)
            calandar_array_for_miladidate.append(t[0])
            calandar_array_for_shamsidate.append(stradby(t[0]))
            t[0] += timedelta(days=1)
        t[0] -=timedelta(days=1)
        return render(request,'calander.html',context={"firstname":firstname_r[0],
                                                       "lastname":lastname_r[0],
                                                       "melicod":melicod_r[0],
                                                       "phonnumber":phonnumber_r[0],
                                                        "year" : year[0],
                                                        "mounth": mounth,
                                                        "calandar_aray":calandar_array_for_show,
                                                       })
    if button_send == 'accept':
        import os
        import matplotlib as mpl
        if os.environ.get("DISPLAY",'') == '' :
            print('no display found. Using non-intractive Agg backebd')
            mpl.use('Agg')
        import matplotlib.pyplot as plt

        print("qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq")
        root = tkinter.Tk()
        print("rrrrrrrrrr")
        root.withdraw()
        print("eeeeeeee")
        messagebox.showerror("error","error message")
        messagebox.showwarning("warning","warning message")
        messagebox.showinfo("information","informative message")

        # accuntmodel.objects.create(firstname=firstname_r[0],
        #                            lastname=lastname_r[0],
        #                            melicode=melicod_r[0],
        #                            phonnumber=phonnumber_r[0],
        #                            berthday=berthmiladi_r[0]
        #                            )
        # return redirect('/')

    return render(request,'add_cantact.html')
def logindef(request):

    return render(request,'login_cantact.html')
def ignordef(request):
    return render(request,'ignor_cantact.html')
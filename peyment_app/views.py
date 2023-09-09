from django.shortcuts import render , redirect
from django.views import View
import requests
from django.conf import settings
import requests
import json
from django.http import HttpResponse
from reserv_app.models import reservemodeltest,reservemodel,neurseformmodel,neurseformtestmodel
from cantact_app.models import accuntmodel


result = ["t"]

class OrderPageView(View):
    def get(self, request):
        return render(request,'reserv_end.html')



amount = 1000  # Rial / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
phone = 'YOUR_PHONE_NUMBER'  # Optional
# Important: need to edit for realy server.
CallbackURL = 'http://127.0.0.1:8000/zib/verify/'
merchandzibal = "zibal"
#? sandbox merchant
if settings.SANDBOX:
    sandbox = 'sandbox'
else:
    sandbox = 'www'
ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"

class OrderPayView(View):
    def get(self,request):
        data = {
            "MerchantID": settings.MERCHANT,
            "Amount": amount,
            "Description": description,
            "Phone": phone,
            "CallbackURL": CallbackURL,
        }
        data = json.dumps(data)
        headers = {'content-type': 'application/json', 'content-length': str(len(data)) }
        res = requests.post(ZP_API_REQUEST, data=data,headers=headers)
        if res.status_code == 200 :
            response = res.json()
            if response['Status'] == 100 :
                url = f"{ZP_API_STARTPAY}{response['Authority']}"
                return redirect(url)
        else:
            print(res.json()['errors'])
            return HttpResponse(str(res.json()['errors']))
class VerifyPayView(View):
    def get(self,request):
        authority = request.GET['Authority']
        data = {
            "MerchantID": settings.MERCHANT,
            "Amount": amount,
            "Authority" : authority,
        }
        data = json.dumps(data)
        headers = {'content-type': 'application/json', 'content-length': str(len(data)) }
        res = requests.post(ZP_API_VERIFY, data=data,headers=headers)
        if res.status_code == 200 :
            response = res.json()
            if response['Status'] == 100 :
                return HttpResponse({'Status': response['Status'],'RefID':response['RefID']})
            else:
                return HttpResponse({'Status': response['Status'],'RefID':response['RefID']})
        else:
            return HttpResponse('پرداخت ناموفق')






# Irandargah_request_url = f"https://dargaah.com/payment"
# merchand_irandargah='69097262-cc95-4999-9d6c-2fe5865bb891'
# Irandargah_send_url="https://dargaah.com/ird/startpay/"
# Irandargah_verify_url='https://dargaah.com/verification'
Irandargah_request_url = f"https://dargaah.com/sandbox/payment"
merchand_irandargah='TEST'
Irandargah_send_url="https://dargaah.com/sandbox/ird/startpay/"
Irandargah_verify_url="https://dargaah.com/sandbox/verification"
# callbackirandargaah = 'http://drmahdiasadpour.ir/zib/irandargahcallback/'
callbackirandargaah = 'http://127.0.0.1:8000/zib/irandargahcallback/'
class OrderPayViewirandagaah(View):
    def get(self,request):
        data = {
            'merchantID': merchand_irandargah,
            'amount': 10000,  # amount of transaction in rial (amount must be between 10,000 and 500,000,000 rial)
            'callbackURL': callbackirandargaah,
            'orderId': '1234',  # you can set your desired unique order id for transaction
            'mobile': '09122852099',  # for more information in transaction's detail // OPTIONAL
            'description': 'YOUR DESCRIPTION'  # for more information in transaction's detail // OPTIONAL
        }
        data = json.dumps(data)
        url = Irandargah_request_url
        headers = {'content-type': 'application/json', 'content-length': str(len(data)) }
        res = requests.post(url, data=data,headers=headers)
        if res.status_code == 200 :
            response = res.json()
            urll = f"{Irandargah_send_url}{response['authority']}"
            return redirect(urll)
        else:
            return HttpResponse(str(res.json()['message']))
# ++++++++++++++++\
class Verifyi(View):
    def get(self,request):
        if request.POST['code'] == 100:
            data = {
                'merchantID': merchand_irandargah,
                'authority': request.POST['authority'],
                'amount': int(request.POST['amount']),
                'orderId': request.POST['orderId'],
            }
            data = json.dumps(data)
            url = Irandargah_request_url
            headers = {'content-type': 'application/json', 'content-length': str(len(data)) }
            res = requests.post(url, data=data, headers=headers)
            if res.status_code == 200 :
                response = res.json()
                if response['Status'] == 100 :
                    return HttpResponse({'Status': response['Status'],'RefID':response['RefID']})
                else:
                    return HttpResponse({'Status': response['Status'],'RefID':response['RefID']})
            else:
                return HttpResponse('پرداخت ناموفق')

        else:
            print('error in transaction\'s payment: ' + request.POST['message'])
            return render(request, 'test.html')




ZIB_API_REQUEST = "https://gateway.zibal.ir/v1/request"
ZIB_API_VERIFY = "https://gateway.zibal.ir/verify"
ZIB_API_STARTPAY = "https://gateway.zibal.ir/start/"
# callbackzibalurl = 'http://127.0.0.1:8000/zib/verifyzibal/'
# merchanzibal = 'zibal'
callbackzibalurl = 'http://mahdiasadpour.ir/zib/verifyzibal/'
merchanzibal = '64c2047fcbbc270017f4c6b2'
m=["0"]
peyment = 50000
def orderzibal(request):
    if request.user.is_authenticated:
        users = accuntmodel.objects.all()
        for user in users:
            if user.melicode == request.user.username:
                phonnumber = user.phonnumber
                m[0] = user.melicode
    data = {
        "merchant": merchanzibal,
        "amount": peyment,
        "callbackUrl": callbackzibalurl,
        "description": "بیعانه جهت رزرو",
        "orderId": "ZBL-7799",
        "mobile": phonnumber
    }
    data = json.dumps(data)
    headers = {'content-type': 'application/json', 'content-length': str(len(data))}
    res = requests.post(ZIB_API_REQUEST, data=data, headers=headers)
    r = res.json()
    if res.status_code == 200:
        if r['result'] == 100:
            url = f"{ZIB_API_STARTPAY}{r['trackId']}"

            return redirect(url)
    else:
        return HttpResponse(str(res.json()['errors']))

    def get(self,request):
        authority = request.GET['Authority']
        data = {
            "MerchantID": settings.MERCHANT,
            "Amount": amount,
            "Authority" : authority,
        }
        data = json.dumps(data)
        headers = {'content-type': 'application/json', 'content-length': str(len(data)) }
        res = requests.post(ZP_API_VERIFY, data=data,headers=headers)
        if res.status_code == 200 :
            response = res.json()
            if response['Status'] == 100 :
                return HttpResponse({'Status': response['Status'],'RefID':response['RefID']})
            else:
                return HttpResponse({'Status': response['Status'],'RefID':response['RefID']})
        else:
            return HttpResponse('پرداخت ناموفق')


def callbackzibal(request):
    trac = request.GET['trackId']
    data = {
        "merchant": merchanzibal,
        "trackId": trac
    }
    data = json.dumps(data)
    headers = {'content-type': 'application/json', 'content-length': str(len(data))}
    res = requests.post(ZIB_API_VERIFY, data=data, headers=headers)
    if res.status_code == 200:
        r = res.json()
        result[0] =r['message']
        result.append(r['cardNumber'])
        # print(r['message'])
        # print(r['result'])
        # print(r['status'])
        # print(r['refNumber'])
        # print(r['description'])
        # print(r['cardNumber'])
        # print(r['orderId'])
    if result[0] == "success":
        reserve = reservemodeltest.objects.all()
        for r in reserve :
            if r.mellicode == m[0]:
                reservemodel.objects.create(jobreserv=r.jobreserv,
                                            detalereserv=r.detalereserv,
                                            personreserv=r.personreserv,
                                            timereserv=r.timereserv,
                                            castreserv=r.castreserv,
                                            hourreserv=r.hourreserv,
                                            dateshamsireserv=r.dateshamsireserv,
                                            datemiladireserv=r.datemiladireserv,
                                            yearshamsi=r.yearshamsi,
                                            cardnumber="result[1]",
                                            pyment=peyment,
                                            )
                a = reservemodeltest.objects.filter(mellicode=m[0])
                a.delete()
        neurse = neurseformtestmodel.objects.all()
        for r in neurse :
            if r.mellicode == m[0]:
                neurseformmodel.objects.create(
                    mellicode=m[0],
                    inject_botax=r.inject_botax,
                    illnes=r.illnes,
                    drug=r.drug,
                    sensivety=r.sensivety,
                    pregnancy=r.pregnancy,
                    date_finaly=r.date_finaly,
                    image_full=r.image_full,
                    image_semi=r.image_semi,
                    image_not=r.image_not,
                    satisfact=r.satisfact,
                )
                a = neurseformtestmodel.objects.filter(mellicode=m[0])
                a.delete()

    # return redirect('http://127.0.0.1:8000/zib/end/')
    return redirect('http://mahdiasadpour.ir/zib/end/')

def end(request):


    return render(request,'end.html',context={"result":result})
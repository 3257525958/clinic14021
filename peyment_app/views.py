from django.shortcuts import render , redirect
from django.views import View
import requests
from django.conf import settings
import requests
import json
from django.http import HttpResponse

#? sandbox merchant
if settings.SANDBOX:
    sandbox = 'sandbox'
else:
    sandbox = 'www'


ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"



Irandargah_request_url = f"https://dargaah.com/payment"


amount = 1000  # Rial / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
phone = 'YOUR_PHONE_NUMBER'  # Optional
# Important: need to edit for realy server.
CallbackURL = 'http://127.0.0.1:8000/zib/verify/'
callbackirandargaah = 'http://drmahdiasadpour.ir/zib/irandargahcallback/'



class OrderPageView(View):
    def get(self, request):
        return render(request,'reserv_end.html')

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




class OrderPayViewirandagaah(View):
    def get(self,request):
        data = {
            'merchantID': '69097262-cc95-4999-9d6c-2fe5865bb891',
            'amount': 10000,  # amount of transaction in rial (amount must be between 10,000 and 500,000,000 rial)
            'callbackURL': callbackirandargaah,
            'orderId': '1234',  # you can set your desired unique order id for transaction
            'mobile': '09122852099',  # for more information in transaction's detail // OPTIONAL
            'description': 'YOUR DESCRIPTION'  # for more information in transaction's detail // OPTIONAL
        };

        url = "https://dargaah.com/payment"

        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
        }
        response = requests.request("POST", url, headers=headers, data=json.dumps(data))

        result = json.loads(response.text)
        print(result['status'])
        if result['status'] == 200:
            url ="https://dargaah.com/ird/startpay/"+result['authority']
            return redirect(url)
            # print("Location: https://dargaah.com/ird/startpay/" + result['authority'])
        else:
            print("Error in connecting to gateway: " + result['message'])
            return render(request,'home.html')


class Verifyi(View):
    def get(self,request):
        print("0000000000")
        print(request)
        if 'code' not in request.POST:
            raise Exception('callback has not valid data')
        print(request.POST['code'])
        if request.POST['code'] == 100:
            data = {
                'merchantID': '69097262-cc95-4999-9d6c-2fe5865bb891',
                'authority': request.POST['authority'],
                'amount': int(request.POST['amount']),
                'orderId': request.POST['orderId'],
            }

            url = 'https://dargaah.com/verification'

            headers = {
                'Content-Type': "application/json",
                'Cache-Control': "no-cache",
            }

            response = requests.request("POST", url, headers=headers, data=json.dumps(data))
            print(response)
            print("999999999")
            result = json.loads(response.text)
            print("1111111111111111")
            print(result['status'])
            if result['status'] == 100:
                print('transaction verified: ' + result['message'])
                print('verification status code: ' + result['status'])
                print('refId: ' + result['refId'])
                print('cardnumber: ' + result['cardNumber'])
                print('order id: ' + result['orderId'])
                return render(request, 'home.html')

            else:
                print('error in transaction\'s payment: ' + result['message'])
                return render(request, 'home.html')
        else:
            print('error in transaction\'s payment: ' + request.POST['message'])
            return render(request,'home.html')

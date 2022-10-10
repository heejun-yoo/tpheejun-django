from django.shortcuts import render

import requests, json, base64, time

# Create your views here.
def index(request):
  return render(
    request,
    'billing/index.html',
  )

def window(request):
  return render(
    request,
    'billing/window.html',
  )

def billing_confirm(request):
  authKey = request.GET.get('authKey')
  customerKey = request.GET.get('customerKey')
  
  url = "https://api.tosspayments.com/v1/billing/authorizations/issue"
  secertkey = "test_sk_D4yKeq5bgrpKRd0JYbLVGX0lzW6Y"
  userpass = secertkey + ':'
  encoded_u = base64.b64encode(userpass.encode()).decode()
  
  headers = {
    "Authorization" : "Basic %s" % encoded_u,
    "Content-Type": "application/json"
  }
  
  params = {
    "authKey" : authKey,
    "customerKey" : customerKey,
  }
  
  res = requests.post(url, data=json.dumps(params), headers=headers)
  resjson = res.json()
  pretty = json.dumps(resjson, indent=4, ensure_ascii=False)

  billingKey = resjson["billingKey"]
  cardCompany = resjson["card"]["company"]
  cardNumber = resjson["card"]["number"]
  

  return render(
    request,
    "billing/billing_confirm.html",
    {
      "res" : pretty,
      "billingKey" : billingKey,
      "cardCompany" : cardCompany,
      "cardNumber" : cardNumber,

    }
  )

def fail(request):
  code = request.GET.get('code')
  message = request.GET.get('message')
  
  return render(
    request,
    "billing/fail.html",
    {
      "code" : code,
      "message" : message,
    }
  )

def billing_auth(request):
  url = "https://api.tosspayments.com/v1/billing/authorizations/card"
  secertkey = "test_sk_D4yKeq5bgrpKRd0JYbLVGX0lzW6Y"
  userpass = secertkey + ':'
  encoded_u = base64.b64encode(userpass.encode()).decode()
  
  headers = {
    "Authorization" : "Basic %s" % encoded_u,
    "Content-Type": "application/json"
  }
  
  params = {
    "customerKey": "test_customer_key",
    "cardNumber": "5531760001177282",
    "cardExpirationYear": "28",
    "cardExpirationMonth": "02",
    "cardPassword": "04",
    "customerBirthday": "871017",
    "customerName": "박토스",
    "customerEmail": "customer@email.com"
  }
  
  res = requests.post(url, data=json.dumps(params), headers=headers)
  resjson = res.json()
  pretty = json.dumps(resjson, indent=4, ensure_ascii=False)

  billingKey = resjson["billingKey"]
  cardCompany = resjson["card"]["company"]
  cardNumber = resjson["card"]["number"]
  

  return render(
    request,
    "billing/billing_auth.html",
    {
      "res" : pretty,
      "billingKey" : billingKey,
      "cardCompany" : cardCompany,
      "cardNumber" : cardNumber,

    }
  )

def billing_approve(request):
  datetime = int(time.time())
  billingKey = "w7EofscBw9WMtNY5D3P9vs4XmkdHn37wF3j4LXme2P4="

  url = "https://api.tosspayments.com/v1/billing/"
  secertkey = "test_sk_D4yKeq5bgrpKRd0JYbLVGX0lzW6Y"
  userpass = secertkey + ':'
  encoded_u = base64.b64encode(userpass.encode()).decode()
  
  headers = {
    "Authorization" : "Basic %s" % encoded_u,
    "Content-Type": "application/json"
  }

  params = {
    "orderId": datetime,
    "amount": 50000,
    "customerKey": "test_customer_key",
    "orderName": "토스 정기 결제",
    "customerName": "박토스",
    "customerEmail": "customer@email.com"
  }

  res = requests.post(url+billingKey, data=json.dumps(params), headers=headers)
  resjson = res.json()
  pretty = json.dumps(resjson, indent=4, ensure_ascii=False)

  return render(
    request,
    'billing/billing_approve.html',
    {
      "res" : pretty,
    }
  )
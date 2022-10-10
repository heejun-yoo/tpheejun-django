from django.shortcuts import render
 
import requests, json, base64, time

# Create your views here.
def index(request):
  return render(
    request,
    'payments/index.html',
  )

def window(request):
  return render(
    request,
    'payments/window.html',
  )

def easypay(request):
  return render(
    request,
    'payments/easypay.html',
  )

def direct(request):
  return render(
    request,
    'payments/direct.html',
  )

def success(request):
  orderId = request.GET.get('orderId')
  amount = request.GET.get('amount')
  paymentKey = request.GET.get('paymentKey')
  
  url = "https://api.tosspayments.com/v1/payments/confirm"
  secertkey = "test_sk_D4yKeq5bgrpKRd0JYbLVGX0lzW6Y"
  userpass = secertkey + ':'
  encoded_u = base64.b64encode(userpass.encode()).decode()
  
  headers = {
    "Authorization" : "Basic %s" % encoded_u,
    "Content-Type": "application/json"
  }
  
  params = {
    "orderId" : orderId,
    "amount" : amount,
    "paymentKey": paymentKey,
  }
  
  res = requests.post(url, data=json.dumps(params), headers=headers)
  resjson = res.json()
  pretty = json.dumps(resjson, indent=4, ensure_ascii=False)

  respaymentKey = resjson["paymentKey"]
  resorderId = resjson["orderId"]
  rescardcom = resjson["card"]["company"]
  

  return render(
    request,
    "payments/success.html",
    {
      "res" : pretty,
      "respaymentKey" : respaymentKey,
      "resorderId" : resorderId,
      "rescardcom" : rescardcom,

    }
  )

def fail(request):
  code = request.GET.get('code')
  message = request.GET.get('message')
  
  return render(
    request,
    "payments/fail.html",
    {
      "code" : code,
      "message" : message,
    }
  )

def vaapi(request):
  datetime = int(time.time())
  
  url = "https://api.tosspayments.com/v1/virtual-accounts"
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
    "customerEmail": "customer@email.com",
    "customerName": "박토스",
    "orderName": "토스 가상계좌 결제",
    "bank": "국민",
    "validHours": 72,
    "virtualAccountCallbackUrl": "https://webhook.site/8f1dca13-02e7-41d6-a6bb-9c217a73d4a8",
    "customerMobilePhone": "01000001234",
    "useEscrow": False  
  }
  
  res = requests.post(url, data=json.dumps(params), headers=headers)
  resjson = res.json()
  pretty = json.dumps(resjson, indent=4, ensure_ascii=False)

  accountNumber = resjson["virtualAccount"]["accountNumber"]
  bank = resjson["virtualAccount"]["bank"]
  
  return render(
    request,
    "payments/vaapi.html",
    {
      "res" : pretty,
      "accountNumber" : accountNumber,
      "bank" : bank,
      
    }
  )

def keyinapi(request):
  datetime = int(time.time())
  
  url = "https://api.tosspayments.com/v1/payments/key-in"
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
    "customerEmail": "customer@email.com",
    "orderName": "토스 카드정보(키인) 결제",
    "cardNumber": "5531760001177282",
    "cardExpirationYear": "28",
    "cardExpirationMonth": "02",
    "cardPassword": "04",
    "customerIdentityNumber": "871017",
    "cardInstallmentPlan": "0",
  }
  
  res = requests.post(url, data=json.dumps(params), headers=headers)
  resjson = res.json()
  pretty = json.dumps(resjson, indent=4, ensure_ascii=False)

  method = resjson["method"]
  number = resjson["card"]["number"]
  
  return render(
    request,
    "payments/keyinapi.html",
    {
      "res" : pretty,
      "method" : method,
      "number" : number,
      
    }
  )

def inquiryapi(request):
  paymentKey = "Ae75jWNka9lpP2YxJ4K87qKoAvN9vVRGZwXLObgyB0vMDm1d"
  
  url = "https://api.tosspayments.com/v1/payments/"
  secertkey = "test_sk_D4yKeq5bgrpKRd0JYbLVGX0lzW6Y"
  userpass = secertkey + ':'
  encoded_u = base64.b64encode(userpass.encode()).decode()
  
  headers = {
    "Authorization" : "Basic %s" % encoded_u,
    "Content-Type": "application/json"
  }
  
  res = requests.get(url+paymentKey, headers=headers)
  resjson = res.json()
  pretty = json.dumps(resjson, indent=4, ensure_ascii=False)
  
  return render(
    request,
    "payments/inquiryapi.html",
    {
      "res" : pretty,
      
    }
  )

def cancelapi(request):
  datetime = int(time.time())
  paymentKey = "ly05n91dEvLex6BJGQOVDx77Rov9kVW4w2zNbgaYRMPoqmDX"
      
  #부분 취소에서만 사용
  cancelAmount = 300
      
  #refundReceiveAccount - 가상계좌 거래에 대해 입금후에 취소하는 경우만 필요
  bank = "국민"
  accountNumber = "12345678901234"
  holderName = "홍길동"

	#중복 취소를 막기위해 취소 가능금액을 전송
  refundableAmount = 300
  
  url = "https://api.tosspayments.com/v1/payments/"
  secertkey = "test_sk_D4yKeq5bgrpKRd0JYbLVGX0lzW6Y"
  userpass = secertkey + ':'
  encoded_u = base64.b64encode(userpass.encode()).decode()
  
  headers = {
    "Authorization" : "Basic %s" % encoded_u,
    "Content-Type": "application/json"
  }
  
  params = {
    "cancelReason": "고객 변심",
    "cancelAmount": cancelAmount,
    #"refundReceiveAccount": {
    #    "bank": bank,
    #    "accountNumber": accountNumber,
    #    "holderName": holderName
    #    }
    #"refundableAmount": refundableAmount
  }
  
  res = requests.post(url+paymentKey+"/cancel", data=json.dumps(params), headers=headers)
  resjson = res.json()
  pretty = json.dumps(resjson, indent=4, ensure_ascii=False)

  orderName = resjson["orderName"]
  method = resjson["method"]
  cancelReason = resjson["cancels"][0]["cancelReason"]
  
  return render(
    request,
    "payments/cancelapi.html",
    {
      "res" : pretty,
      "orderName" : orderName,
      "method" : method,
      "cancelReason" : cancelReason,
      
    }
  )
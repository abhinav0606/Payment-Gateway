# https://dev.to/iiits-iota/paytm-payment-gateway-integration-in-django-1657
# https://www.youtube.com/watch?v=cdtPcTIuazI
# tutorials for the payment gateway........
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def payment(request):
    return render(request,'payment.html')
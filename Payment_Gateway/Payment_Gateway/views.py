from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
import razorpay
from django.views.decorators.csrf import csrf_exempt
def index(request):
    return render(request,"index.html")
def payment(request):
    if request.method=="POST":
        name=request.POST.get("name","")
        amount=request.POST.get("amount","")
        amount=str(int(amount)*100)
        c = razorpay.Client(auth=("rzp_test_wVtLT9v4Tl4TBT","f4HKckt66CMS6gk7qUjDNB79"))
        response=c.order.create({"amount":amount,"currency":"INR", "receipt":'order_rcptid_11',"payment_capture":"1"})
        context={"response":response,"X":str(response["amount"]),"Y":name}
    return render(request,"payment.html",context)
@csrf_exempt
def payment_success(requst):
    if requst.method=="POST":
        print(requst.POST)
        return HttpResponseRedirect("/")

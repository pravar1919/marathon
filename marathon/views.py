from django.http import JsonResponse
from django.shortcuts import render
import razorpay
from .models import Orders



def create_order(receipt):
    client = razorpay.Client(auth=("rzp_test_vmaQRd7HwbR8NZ", "c0YSJJZCBcNitKk6u7V2Zy6v"))
    data = { "amount": 100 * 100, "currency": "INR", "receipt": f"order_{receipt}" }
    payment = client.order.create(data=data)
    return payment

def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        obj = Orders.objects.create(name = name, email=email, phone_number=mobile)
        payment = create_order(obj.id)
        # print(payment)
        return JsonResponse({"payment":payment, "name":name, "email":email, "mobile": mobile})
        
    return render(request, "base.html")
from django.shortcuts import render

# Create your views here.
def place_order(request):
    return render(request,'order/place_order.html')
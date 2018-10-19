from django.shortcuts import render

# Create your views here.
def user_center_info(request):
    return render(request,'user/user_center_info.html')

def user_center_order(request):
    return render(request,'user/user_center_order.html')

def user_center_site(request):
    return render(request,'user/user_center_site.html')
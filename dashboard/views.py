from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'dashboard/index.html')

def staff(request):
    return render(request, 'dashboard/staff.html')

def product(request):
    return render(request, 'dashboard/product.html')

def sales(request):
    return render(request, 'dashboard/sales.html')

def profile(request):
    return render(request, 'dashboard/profile.html')

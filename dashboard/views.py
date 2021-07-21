from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.
@login_required(login_url='user-login')
def index(request):
    return render(request, 'dashboard/index.html')

@login_required(login_url='user-login')
def staff(request):
    return render(request, 'dashboard/staff.html')

@login_required(login_url='user-login')
def product(request):
    return render(request, 'dashboard/product.html')

@login_required(login_url='user-login')
def sales(request):
    return render(request, 'dashboard/sales.html')
    
@login_required(login_url='user-login')
def profile(request):
    return render(request, 'user/profile.html')

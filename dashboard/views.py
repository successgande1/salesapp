from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm, SalesForm

# Create your views here.
@login_required(login_url='user-login')
def index(request):
    return render(request, 'dashboard/index.html')

@login_required(login_url='user-login')
def staff(request):
    return render(request, 'dashboard/staff.html')


#Method for Add and Displaying Products
@login_required(login_url='user-login')
def product(request):

    items = Product.objects.all() #Using ORM
    #items = Product.objects.raw('SELECT * FROM Dashboard_Product')
    #Check whether form is post via POST Method
    if request.method == 'POST':
        add_product_form = ProductForm(request.POST)
        #Check if form is valid
        if add_product_form.is_valid:
            add_product_form.save()
            return redirect('dashboard-product')
    else:
        add_product_form = ProductForm()

    context = {
        'items':items,
        'add_product_form':add_product_form,
    }
    return render(request, 'dashboard/product.html', context)

@login_required(login_url='user-login')
def sales(request):
    return render(request, 'dashboard/sales.html', context)
    
@login_required(login_url='user-login')
def profile(request):
    return render(request, 'user/profile.html')

#Method for Deleting Product
def product_delete(request, pk):
    #Grab a particular Item by item
    items = Product.objects.get(id=pk)
    if request.method == 'POST':
        items.delete()
        return redirect('dashboard-product')
    return render(request, 'dashboard/product_delete.html')

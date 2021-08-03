from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Product, Sales
from .forms import ProductForm, SalesForm
from django.contrib.auth.models import User


from django.contrib import messages

# Create your views here.
@login_required(login_url='user-login')
def index(request):
    return render(request, 'dashboard/index.html')

#METHOD FOR DISPLAYING LIST OF STAFF
@login_required(login_url='user-login')
def staff(request):
    workers = User.objects.all()

    context = {
        'workers':workers
    }
    return render(request, 'dashboard/staff.html', context)


#METHOD FOR DISPLAYING STAFF DETAIL
@login_required(login_url='user-login')
def staff_detail(request, pk):
    worker = User.objects.get(id=pk)
    context = {
        'worker':worker
    }
    return render(request, 'dashboard/staff_detail.html', context)

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
            #Notify User on Product Save
            messages.success(request, 'Product Added Successfully')
            return redirect('dashboard-product')
    else:
        add_product_form = ProductForm()

    context = {
        'items':items,
        'add_product_form':add_product_form,
    }
    return render(request, 'dashboard/product.html', context)

#Add and Display Sales Method
@login_required(login_url='user-login')
def sales(request):
    #List of Sales
    orders = Sales.objects.all()
    
    if request.method == 'POST':
        Sales_Form = SalesForm(request.POST)
        if Sales_Form.is_valid:
            Sales_Form.save()
            messages.success(request, 'Sales Added Successfully')
            return redirect('dashboard-sales')
    else:
        Sales_Form = SalesForm()
    context = {
        'orders':orders, 
        'Sales_Form':Sales_Form,
    }
    return render(request, 'dashboard/sales.html', context)
    
@login_required(login_url='user-login')
def profile(request):
    return render(request, 'user/profile.html')

#Method for Deleting Product
@login_required(login_url='user-login')
def product_delete(request, pk):
    #Grab a particular Item by item
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        #Notify User on Product delete
        messages.error(request, f'{item} Product Deleted Successfully')
        return redirect('dashboard-product')
    context = {
        'item' : item,
    }
    return render(request, 'dashboard/product_delete.html', context)

#Update Product Detail
@login_required(login_url='user-login')
def product_update(request, pk):
    #Create an item variable and capture a product using its id
    item = Product.objects.get(id=pk)
    #Check if the user request method is through POST
    if request.method == 'POST':
        #Create Product Update Form Variable and call the ProductForm class method
        #and pass in the request.POST with an instance of the Product with particular id
        product_update_form = ProductForm(request.POST, instance=item)
        #If the Product Update form is valid
        if product_update_form.is_valid():
            #Save the Product Update Form using the save method
            product_update_form.save()
            #Redirect to the Dashboard
            messages.success(request, f'{item} Updated Successfully')
            return redirect('dashboard-product')
    else:
        product_update_form = ProductForm(instance=item)

    context = {
        'item':item,
        'product_update_form':product_update_form,
    }
    return render(request, 'dashboard/product_update.html', context)





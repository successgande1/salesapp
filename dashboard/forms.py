from django import forms
from .models import Product
from .models import Sales

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'cost', 'price', 'quantity']

class SalesForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = ['product', 'customer', 'quantity']
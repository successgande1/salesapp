from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
CATEGORY = (
    ('Stationaries', 'Stationaries'),
    ('Electronics', 'Electronics'),
    ('Food', 'Food'),
    ('Wears', 'Wears'),
)
class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100, choices=CATEGORY, null=True)
    cost = models.PositiveIntegerField(null=True)
    price = models.PositiveIntegerField(null=True)
    quantity = models.PositiveIntegerField(null=True)

    class Meta:
        verbose_name_plural = 'Product'

    def __str__(self):
        return self.name

class Sales(models.Model): 
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    customer = models.CharField(max_length=30, null=True)
    quantity = models.PositiveIntegerField(null=True)
    price = models.PositiveIntegerField(null=True)
    salesdate = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Product Sales'

    def __str__(self):
        return self.customer

from django.db import models

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
    costprice = models.PositiveIntegerField(null=True)
    sellingprice = models.PositiveIntegerField(null=True)
    quantity = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.name
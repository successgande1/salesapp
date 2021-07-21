# Generated by Django 3.2.5 on 2021-07-21 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20210721_0908'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='costprice',
            new_name='cost',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='sellingprice',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='sales',
            old_name='salesqty',
            new_name='quantity',
        ),
        migrations.RemoveField(
            model_name='sales',
            name='sellingprice',
        ),
    ]

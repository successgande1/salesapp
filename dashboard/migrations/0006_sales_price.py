# Generated by Django 3.2.5 on 2021-07-30 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20210721_0914'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='price',
            field=models.PositiveIntegerField(null=True),
        ),
    ]

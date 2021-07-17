from django.urls import path

from . import views

urlpatterns = [
    path('dashboard/', views.index, name = 'dashboard-index'),
    path('staff/', views.staff, name = 'dashboard-staff'),
    path('product/', views.product, name = 'dashboard-product'),
    path('sales/', views.sales, name = 'dashboard-sales'),
    path('profile/', views.profile, name = 'dashboard-profile'),
]
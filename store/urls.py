from django.urls import path,include
from .import views

urlpatterns=[
    path('', views.store, name ='store'),
    path('cart/', views.cart, name ='cart'),
    path('checkout/', views.checkout, name ='checkout'),
    path('update_item/', views.updateItem, name ='update_item'),
    path('process_order/',views.processorder, name ='process_order')
]
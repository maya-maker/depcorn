from django.contrib import admin
from django.urls import path
from backend.views import register,add_to_cart,login,index,logout,cartitem,cartremove,order_place,payment

urlpatterns = [
    path('',index,name='index'),
    path('register/',register,name='register'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('cart/<str>/<int:id>',add_to_cart,name='cart'),
    path('cartitem/<str>',cartitem,name='cartitem'),
    path('cartitem/Remove/<int:id>',cartremove,name='cartremove'),
    path('cartitem/order_placed/<str>/<str2>/<str3>',order_place,name='order_placed'),
    path('cartitem/order_placed/<q>/<p>/payment',payment)
]

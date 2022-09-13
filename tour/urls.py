from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.home, name="home"),

    path('daytrip/', views.daytrip, name="daytrip"),

    path('index/', views.index, name="index"),

    path('about/', views.about, name="about"),

    path('gallery/', views.gallery, name="gallery"),

    path('contact/', views.contact, name="contact"),

    path('destination/', views.destination, name="destination"),

    path('product_detail/', views.product_detail, name="product_detail"),

    path('product_detailone/', views.product_detailone, name="product_detailone"),

    path('product_detailtwo/', views.product_detailtwo, name="product_detailtwo"),

    path('product_detailthree/', views.product_detailthree, name="product_detailthree"),

    path('product_detailfour/', views.product_detailfour, name="product_detailfour"),

    path('product_detailfive/', views.product_detailfive, name="product_detailfive"),

    path('product_detailsix/', views.product_detailsix, name="product_detailsix"),

    path('product_detailseven/', views.product_detailseven, name="product_detailseven"),

    path('product_detaileight/', views.product_detaileight, name="product_detaileight"),

    path('product_detailnine/', views.product_detailnine, name="product_detailnine"),

     path('booking/', views.booking, name="booking"),

]    
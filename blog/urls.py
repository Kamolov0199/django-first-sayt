from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('asosiy/', asosiy),
    path('asosiy/cars1.html/', ferrary),
    path('asosiy/cars2.html/', mersedes),
    path('asosiy/cars3.html/', bmv),
    path('asosiy/cars4.html/', toyota),
    path('asosiy/cars5.html/', mers),
    path('asosiy/cars6.html/', nissan)
]


from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    # welcome home messgae
    path('', welcomeHome, name='home'),

    # url to calculator function
    path('api/function/', include(('calculator.urls','calculator'),namespace='calculator')),
]

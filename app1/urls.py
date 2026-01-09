from django.urls import path
from .views import *


urlpatterns=[
    path('',Home),
    path('register.html',Reg)
]
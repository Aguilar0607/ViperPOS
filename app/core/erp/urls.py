from django.contrib import admin
from django.urls import path
from core.erp.views import myfirstview

urlpatterns = [
    path('one/', myfirstview),
    path('two/', myfirstview)
]
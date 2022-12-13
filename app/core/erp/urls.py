from django.contrib import admin
from django.urls import path
from core.erp.views import myfirstview, mysecondview

app_name = 'erp'

urlpatterns = [
    path('one/', myfirstview, name='view1'),
    path('two/', mysecondview, name='view2')
]
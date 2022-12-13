from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from core.erp.models import *
# Create your views here.

def myfirstview(request):
    data = {
        'name': 'Blaze',
        'categories': Category.objects.all()
    }
    return render(request, 'index.html', data)

def mysecondview(request):
    data = {
        'name': 'Blaze',
        'products': Product.objects.all(),
        'categories': Category.objects.all()
    }
    return render(request, 'second.html', data)
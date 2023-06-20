import datetime

from django.http import HttpRequest
from django.shortcuts import render

from . import forms, models

def reserve_del(request):
    models.User.objects.filter(id=reserve_id).delete()
    return menberinfo(request)

def register(request):
    register_form = forms.Register_Form()
    context = {'register_form': register_form}
    return render(request, 'register.html', context)

def register_check(request):
    register_form = forms.Register_Form(request.POST)
    if register_form.is_valid():
        models.User.objects.create(
            
        )
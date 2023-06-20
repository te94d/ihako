import datetime

from django.http import HttpRequest
from django.shortcuts import render

from .. import forms, models



def register(request):
    register_form = forms.Register_Form()
    context = {'register_form': register_form}
    return render(request, 'register.html', context)

def register_check(request):
    register_form = forms.Register_Form(request.POST)
    if register_form.is_valid():
        models.User.objects.create(
            name = register_form.cleaned_data['name'],
            email = register_form.cleaned_data['email'],
            password = register_form.cleaned_data['password'],
            birth = register_form.cleaned_data['birth'],
            address = register_form.cleaned_data['address'],
            phone_num = register_form.cleaned_date['phone_num'],
        )
        member = models.User.objects.get(
            username=register_form.cleaned_data['username']
        )
        context = {'member': member}
        return render(request, 'registercheck.html', context
            )

    return hukumitsu(request)
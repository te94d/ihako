from django.shortcuts import render
from . import forms

# Create your views here.

#ログインページの表示
def login(request):
    login_form = forms.login_form()
    return render(request, 'login.html', context={'login_form':login_form})

#ログアウト
def logout(request):
    request.session.flush()
    return login(request)
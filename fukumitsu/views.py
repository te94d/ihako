from django.shortcuts import render
from . import forms
from . import models

# Create your views here.

#TOP
def fukumitsu(request):
    return render(request, 'fukumitsu.html')

#ログインページの表示
def login(request):
    login_form = forms.login_form()
    return render(request, 'login.html', context={'login_form':login_form})

#ログイン分岐
def login_sep(request):
    if 'email' not in request.session:
        login_form = forms.login_form(request.POST)
        if login_form.is_valid():
            try:
                login_user = models.User.objects.get(
                    email = login_form.cleaned_data['email'],
                    password = login_form.cleaned_data['password']
                    )
                if login_form.cleaned_data['email'] == login_user.email and login_form.cleaned_data['password'] == login_user.password:
                    request.session['email'] = login_form.cleaned_data['email']
                    return render(request, 'fukumitsu.html')
                else:
                    return render(request, 'loginerror.html')
            except(models.User.DoesNotExist, models.User.MultipleObjectsReturned):
                return render(request, 'loginerror.html')   
        else:
            return render(request, 'loginerror.html')
    else:
         return render(request, 'fukumitsu.html')

#ログアウト
def logout(request):
    request.session.flush()
    return login(request)

#管理者画面の表示
def admin_forms(request):
    information_form = forms.information_form()
    sightseeing_form = forms.sightseeing_form()
    admin_forms = {'information_form':information_form, 'sightseeing_form':sightseeing_form}
    return render(request, 'admin.html', context = admin_forms)

#管理者 - お知らせの追加機能
def info_add(request):
    information_form = forms.information_form(request.POST)
    
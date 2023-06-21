from django.shortcuts import render
from . import forms
from . import models
import datetime

# Create your views here.

#TOP
def fukumitsu(request):
    #お知らせの読み込み
    info_list = models.Information.objects.all().order_by().reverse()[:5]
    #お問い合わせフォーム
    contact_form = forms.contact_form()
    if 'email' not in request.session:
        context_data = {'info_list': info_list, 'contact_form':contact_form, 'session':0}
        return render(request, 'fukumitsu.html', context= context_data)
    else:
        context_data = {'info_list': info_list, 'contact_form':contact_form, 'session':1}
        return render(request, 'fukumitsu.html', context= context_data)

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
                administrator = models.User.objects.get(user_id = 1)
                login_user = models.User.objects.get(email = login_form.cleaned_data['email'], password = login_form.cleaned_data['password'])
                if login_form.cleaned_data['email'] == administrator.email and login_form.cleaned_data['password'] == administrator.password: #メアドがアドミンじゃなければ管理者画面へ遷移
                    request.session['email'] = login_form.cleaned_data['email']
                    return admin_forms(request)
                elif login_form.cleaned_data['email'] == login_user.email and login_form.cleaned_data['password'] == login_user.password:
                    request.session['email'] = login_form.cleaned_data['email']
                    return fukumitsu(request)
                else:
                    context_data = 0
                    return render(request, 'loginerror.html')
            except(models.User.DoesNotExist, models.User.MultipleObjectsReturned):
                context_data = 0
                return render(request, 'loginerror.html', context={'session':context_data})   
        else:
            context_data = 0
            return render(request, 'loginerror.html', context={'session':context_data}) 
    else:
        return fukumitsu(request)

#ログアウト
def logout(request):
    request.session.flush()
    return login(request)

#管理者画面の表示
def admin_forms(request):
    information_form = forms.information_form()
    sightseeing_form = forms.sightseeing_form()
    context_data = 1
    info_list = models.Information.objects.all()
    sight_list = models.Sightseeing.objects.all()
    contact_list = models.Contact_us.objects.all()
    admin_forms = {
            'information_form':information_form,
            'sightseeing_form':sightseeing_form,
            'session':context_data,
            'info_list':info_list,
            'sight_list':sight_list,
            'contact_list':contact_list,
            }
    return render(request, 'admin.html', context = admin_forms)

#管理者 - お知らせの追加機能
def info_add(request):
    information_form = forms.information_form(request.POST)
    print(information_form)
    if information_form.is_valid():
        category = information_form.cleaned_data['category']
        contents = information_form.cleaned_data['contents']
        models.Information.objects.create(category = category, contents = contents, time = datetime.date.today())
    return admin_forms(request)

#お知らせの削除機能
def info_del(request, information_id):
    models.Information.objects.filter(information_id = information_id).delete()
    return admin_forms(request)

#管理者 - 観光地の追加機能
def sight_add(request):
    sightseeing_form = forms.sightseeing_form(request.POST)
    if sightseeing_form.is_valid():
        name = sightseeing_form.cleaned_data['name']
        contents = sightseeing_form.cleaned_data['contents']
        filename = sightseeing_form.cleaned_data['filename']
        models.Sightseeing.objects.create(name = name, contents = contents, filename = filename)
    return admin_forms(request)

#観光地の削除機能
def sight_del(request, sightseeing_id):
    models.Sightseeing.objects.filter(sightseeing_id = sightseeing_id).delete()
    return admin_forms(request)

#予約の削除機能
def reservedelete(request, reserve_id):
    models.Reserve.objects.filter(reserve_id = reserve_id).delete()
    return memberinfo(request)

#お問い合わせフォーム
def contact_us(request):
    contact_form = forms.contact_form(request.POST)
    if contact_form.is_valid():
        name = contact_form.cleaned_data['name']
        email = contact_form.cleaned_data['email']
        contents = contact_form.cleaned_data['contents']
        models.Contact_us.objects.create(name = name, email = email, contents = contents)
    return fukumitsu(request)

#お問い合わせの削除機能
def contact_del(request, contact_id):
    models.Contact_us.objects.filter(contact_id = contact_id).delete()
    return admin_forms(request)

#会員登録フォーム
def register(request):
    member_form = forms.member_form()
    context_date = {'register_form': member_form}
    return render(request, 'register.html', context = context_date)

#会員登録の最終確認ページ
def register_check(request):
    member_form = forms.member_form(request.POST)
    if member_form.is_valid():
        request.session['name'] = member_form.cleaned_data['name']
        request.session['email'] = member_form.cleaned_data['email']
        request.session['password'] = member_form.cleaned_data['password']
        request.session['birth'] = str(member_form.cleaned_data['birth'])
        request.session['address'] = member_form.cleaned_data['address']
        request.session['phone_num'] =  member_form.cleaned_data['phone_num']
    context_date={
        "name":request.session['name'],
        "email":request.session['email'],
        "password":request.session['password'],
        "birth":request.session['birth'],
        "address":request.session['birth'],
        "phone_num":request.session['phone_num'],
    }
    return render(request,"registercheck.html",context=context_date)

#データベースへの会員登録
def register_member(request):
        models.User.objects.create(
            name = request.session['name'],
            email = request.session['email'],
            password = request.session['password'],
            birth = request.session['birth'],
            address = request.session['address'],
            phone_num = request.session['phone_num'],
        )
        del request.session['name'],
        del request.session['email'],
        del request.session['password'],
        del request.session['birth'],
        del request.session['address'],
        del request.session['phone_num'],
        return login(request)

#会員ページ - 予約情報の確認
def memberinfo(request):
    login_user_info = models.User.objects.get(email =request.session['email'] )
    future_reserve = models.Reserve.objects.filter(check_in__gte = datetime.date.today(),user_id = login_user_info.user_id)    
    context_data = {"login_user_info":login_user_info,"future_reserve":future_reserve}
    return render(request, "memberinfo.html",context=context_data)

#予約削除前確認ページ
def reservedeletecheck(request,reserve_id):
    delete_reserve = models.Reserve.objects.get(reserve_id = reserve_id)
    context_data = {"delete_reserve": delete_reserve,}
    return render(request, "reservedelete.HTML",context=context_data)

#観光地ページの表示
def sightseeing(request):
    sight_list = models.Sightseeing.objects.all()
    context_data = {'sight_list':sight_list}
    return render(request, 'sightseeing.html', context=context_data)

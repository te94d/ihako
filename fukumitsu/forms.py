from django import forms

#顧客入力用フォーム

#名前とパスワードの入力フォーム
class login_form(forms.Form):
    email = forms.EmailField(widget= forms.TextInput(), required=True)
    password = forms.CharField(widget= forms.PasswordInput(), required=True)

#会員登録用フォーム
class member_form(forms.Form):
    name = forms.CharField(widget= forms.TextInput(), required=True)
    email = forms.EmailField(widget= forms.EmailInput(), required=True)
    password = forms.CharField(widget= forms.PasswordInput(), required=True)
    birth = forms.DateField(widget= forms.DateInput(), required=False)
    address = forms.CharField(widget= forms.TextInput(), required=False)
    phone_num = forms.IntegerField(widget= forms.NumberInput(), required=False)

#家族構成登録フォーム
class family_form(forms.Form):
    name1 = forms.CharField(widget= forms.TextInput(), required=False)
    relationship1 = forms.CharField(widget= forms.TextInput(), required=False)
    birth1 = forms.DateField(widget= forms.DateInput(),required=False)
    name2 = forms.CharField(widget= forms.TextInput(), required=False)
    relationship2 = forms.CharField(widget= forms.TextInput(), required=False)
    birth2 = forms.DateField(widget= forms.DateInput(), required=False)
    name3 = forms.CharField(widget= forms.TextInput(), required=False)
    relationship3 = forms.CharField(widget= forms.TextInput(), required=False)
    birth3 = forms.DateField(widget= forms.DateInput(), required=False)
    name4 = forms.CharField(widget= forms.TextInput(), required=False)
    relationship4 = forms.CharField(widget= forms.TextInput(), required=False)
    birth4 = forms.DateField(widget= forms.DateInput(), required=False)
    name5 = forms.CharField(widget= forms.TextInput(), required=False)
    relationship5 = forms.CharField(widget= forms.TextInput(), required=False)
    birth5 = forms.DateField(widget= forms.DateInput(), required=False)

#予約検索フォーム
class reservedate_form(forms.Form):
    check_in = forms.DateField(widget= forms.DateInput(), required=True)
    check_out = forms.DateField(widget= forms.DateInput(), required=True)
    stay_people = forms.IntegerField(widget= forms.NumberInput(), required=True)

#お問い合わせフォーム
class contact_form(forms.Form):
    name = forms.CharField(widget= forms.TextInput(), required=True)
    email = forms.EmailField(widget= forms.EmailInput(), required=True)
    contents = forms.CharField(widget= forms.TextInput(), required=True)

#管理者画面用フォーム

#お知らせの追加フォーム
class information_form(forms.Form):
    category = forms.CharField(widget= forms.TextInput(), required=True)
    contents = forms.CharField(widget= forms.TextInput(), required=True)

#観光情報追加フォーム
class sightseeing_form(forms.Form):
    name = forms.CharField(widget= forms.TextInput(), required=True)
    contents = forms.CharField(widget= forms.TextInput(), required=True)
    filename = forms.CharField(widget= forms.TextInput(), required=True)

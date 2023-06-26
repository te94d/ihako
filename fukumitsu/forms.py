from django import forms
import datetime

#顧客入力用フォーム

#名前とパスワードの入力フォーム
class login_form(forms.Form):
    email = forms.EmailField(label='', widget= forms.TextInput(attrs={'placeholder':'メールアドレス'}), required=True)
    password = forms.CharField(label='', widget= forms.PasswordInput(attrs={'placeholder':'パスワード'}), required=True)

#会員登録用フォーム
class member_form(forms.Form):
    name = forms.CharField(label='', widget= forms.TextInput(attrs={'placeholder':'氏名'}), required=True)
    email_address = forms.EmailField(label='', widget= forms.EmailInput(attrs={'placeholder':'メールアドレス'}), required=True)
    password = forms.CharField(label='', widget= forms.PasswordInput(attrs={'placeholder':'パスワード'}), required=True)
    birth = forms.DateField(label='', widget= forms.NumberInput(attrs={'type':'date'}), required=True)
    address = forms.CharField(label='', widget= forms.TextInput(attrs={'placeholder':'住所'}), required=False)
    phone_num = forms.CharField(label='', widget= forms.NumberInput(attrs={'placeholder':'電話番号'}), required=False)

#家族構成登録フォーム
class family_form(forms.Form):
    name1 = forms.CharField(label='', widget= forms.TextInput(attrs={'placeholder':'氏名'}), required=False)
    relationship1 = forms.CharField(label='', widget= forms.TextInput(attrs={'placeholder':'続柄'}), required=False)
    birth1 = forms.DateField(label='', widget= forms.DateInput(attrs={'placeholder':''}),required=False)
    name2 = forms.CharField(label='', widget= forms.TextInput(), required=False)
    relationship2 = forms.CharField(label='', widget= forms.TextInput(), required=False)
    birth2 = forms.DateField(label='', widget= forms.DateInput(), required=False)
    name3 = forms.CharField(label='', widget= forms.TextInput(), required=False)
    relationship3 = forms.CharField(label='', widget= forms.TextInput(), required=False)
    birth3 = forms.DateField(label='', widget= forms.DateInput(), required=False)
    name4 = forms.CharField(label='', widget= forms.TextInput(), required=False)
    relationship4 = forms.CharField(label='', widget= forms.TextInput(), required=False)
    birth4 = forms.DateField(label='', widget= forms.DateInput(), required=False)
    name5 = forms.CharField(label='', widget= forms.TextInput(), required=False)
    relationship5 = forms.CharField(label='', widget= forms.TextInput(), required=False)
    birth5 = forms.DateField(label='', widget= forms.DateInput(), required=False)

#予約検索フォーム
class reservedate_form(forms.Form):
    check_in = forms.DateField(label= 'チェックイン', widget= forms.NumberInput(attrs={"type": "date",'min':datetime.date.today() }), required=True)
    chack_out = forms.DateField(label= 'チェックアウト',widget= forms.NumberInput(attrs={"type": "date",'min':datetime.date.today() }), required=True)
    list = (
        ('1',1),('2',2),('3',3),('4',4),('5',5),('6',6)
    )
    stay_people = forms.ChoiceField(label= '宿泊人数', required=True, choices=list)

#お問い合わせフォーム
class contact_form(forms.Form):
    name = forms.CharField(label='', widget= forms.TextInput(attrs={'placeholder':'お名前'}), required=True)
    email = forms.EmailField(label='', widget= forms.EmailInput(attrs={'placeholder':'メールアドレス'}), required=True)
    contents = forms.CharField(label='',required=True,max_length=1024,widget=forms.Textarea(attrs={'placeholder': 'お問い合わせ内容を1,024文字以内で入力してください。',}))

#管理者画面用フォーム

#お知らせの追加フォーム
class information_form(forms.Form):
    list = (('お知らせ', 'お知らせ'), ('イベント', 'イベント'), ('緊急', '緊急'))
    category = forms.ChoiceField(label='', required=True, choices=list)
    contents = forms.CharField(label='', widget= forms.TextInput(attrs={'placeholder':'お知らせ内容'}), required=True)

#観光情報追加フォーム
class sightseeing_form(forms.Form):
    name = forms.CharField(label='', widget= forms.TextInput(attrs={'placeholder':'観光地名称'}), required=True)
    filename = forms.CharField(label='', widget= forms.TextInput(attrs={'placeholder':'ファイル名'}), required=True)
    contents = forms.CharField(label='',required=True,max_length=1024,widget=forms.Textarea(attrs={'placeholder': '観光地情報を1,024文字以内で入力してください。',}))

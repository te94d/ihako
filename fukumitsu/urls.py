from django.urls import path
from . import views

urlpatterns = [
    #ユーザ利用画面用
    path('', views.fukumitsu), #トップページ表示
    path('login/', views.login), #ログインページ（ユーザによる分岐あり）
    path('login_sep/', views.login_sep), #ログイン分岐
    path('logout/', views.logout), #ログアウト
    
    # path('reserve/', views.reserve), #宿泊予約検索
    # path('room/', views.room), #予約できる部屋の一覧表示
    # path('reservecheck/', views.reservecheck), #予約確認画面の表示（ログイン有無の分岐あり）
    # path('reservefin/', views.reservefin), #予約完了画面の表示
    # path('register/', views.register), #会員登録画面の表示
    # path('registercheck/', views.registercheck), #会員登録確認画面の表示
    # path('memberinfo/', views.memberinfo), #ユーザ情報の表示
    # path('reservedelete/', views.reservedelete), #予約削除機能
    # path('sightseeing/', views.sightseeing), #観光情報ページの表示
    # path('faq/', views.faq), #FAQの表示
    path('contact_us/', views.contact_us), #お問い合わせの送信機能
    
    # #管理者画面用
    path('admin_forms/', views.admin_forms), #管理者画面の表示
    path('info_add/', views.info_add), #お知らせの追加機能
    path('info_del/<int:information_id>', views.info_del), #お知らせの削除機能
    path('sight_add/', views.sight_add), #観光情報の追加機能
    path('sight_del/<int:sightseeing_id>', views.sight_del), #観光情報の削除機能
    # path('contact_check', views.contact_check), #お問い合わせの確認機能
    path('contact_del/<int:contact_id>', views.contact_del),
    
]
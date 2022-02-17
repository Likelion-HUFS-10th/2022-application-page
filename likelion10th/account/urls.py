from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    #로그아웃 기능인데 혹시 필요할지도 몰라 만들어 보았습니다.
    path('logout/', views.Logout, name='logout'),
    #탈퇴 기능인데 혹시 필요할지도 몰라 만들어 보았습니다.
    path('secession/',views.secession, name='secession'),

    path('login/kakao/', views.kakao_login, name="kakao-login"),
    path('login/kakao/callback/', views.kakao_callback, name='kakao-callback'),
]
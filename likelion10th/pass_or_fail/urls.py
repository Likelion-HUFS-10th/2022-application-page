from django.urls import path
from . import views #현재 폴더에 있는 views에 접근하기 때문

app_name = 'pass_or_fail' # app_name에는 앱 이름을 넣어줍니다.

urlpatterns = [
    
     path('', views.pass_or_fail, name='pass_or_fail'),
     path('anne/', views.anne, name='anne'),
    
]
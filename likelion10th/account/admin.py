from django.contrib import admin
from .models import User

#우리가 배웠던 admin 페이지에 모델을 등록하는 함수가 admin.register이고 이에 User 라는 모델을 담은 것입니다. 
#이에 대한 상세한 설정을 할 수 있도록 해주는 클래스를 따로 지정한 것입니다. 
@admin.register(User)
class Useradmin(admin.ModelAdmin):
    """"Admin View for User"""
    #admin 페이지에서 어떻게 데이터를 볼지 설정하는 것입니다.
    #이름, 이메일, 휴대폰 번호 순으로 우리는 유저의 정보를 볼 수 있게 됩니다. 
    list_display = (
        "name",
        "email",
        "phone_num",
    )


from django.shortcuts import render, get_object_or_404, redirect
import account.models
from django.contrib.auth.decorators import login_required
import datetime

@login_required(login_url='/account/login/')
def pass_or_fail(request):
    release_date = datetime.datetime(2022, 3, 7, 18, 0, 0)
    if datetime.datetime.now() < release_date:  # 현재 시간이 3월 7일 서류 합격 발표날보다 일찍이라면 접근할 수 없음.
        return redirect('home')

    User = request.user #로그인된 유저 뽑아내기
    pass_key = User.is_accepted
    
    if pass_key == False :
        return render(request, 'fail.html')

    else : 
        return render(request, 'pass.html')
       

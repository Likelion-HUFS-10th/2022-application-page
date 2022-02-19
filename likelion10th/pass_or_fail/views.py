from django.shortcuts import render, get_object_or_404, redirect
import account.models
from django.contrib.auth.decorators import login_required

@login_required

def pass_or_fail(request):

    User = request.user #로그인된 유저 뽑아내기

    pass_key = User.is_accepted
    
    if pass_key == False :
        return render(request, 'fail.html')

    else : 
        return render(request, 'pass.html')
       

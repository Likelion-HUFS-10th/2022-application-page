import requests
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from  . import forms
from  django.views.generic import FormView
from  . import models as user_models


class LoginView(FormView):
    template_name="login.html"
    form_class=forms.LoginForm

    def form_valid(self, form):
        email=form.cleaned_data.get('email')
        password=form.cleaned_data.get('password')
        user=authenticate(self.request,username=email, password=password)

        if user is not None:
            login(self.request, user)
            
            print(user)

            return render(self.request, 'home.html')
        return super().form_vaild(form)

class SignUpView(FormView):
    template_name="signup.html"
    form_class=forms.SignUpform

    def form_valid(self,form):
        form.save()
        email=form.cleaned_data.get('email')
        password=form.cleaned_data.get('password')
        user=authenticate(self.request, username=email,password=password)
        if user is not None:
            login(self.request, user)

            return render(self.request, 'home.html')
        super(SignUpView,self).form_valid(form)

#로그아웃함수입니다. 필요시 사용하면 좋을것 같아 만들었습니다.
def Logout(request):

    logout(request)
    
    return render(request, 'home.html')

#탈퇴함수입니다. 필요시 사용하면 좋을것 같아 만들었습니다.
def secession(request):
    if request.method=='POST':
        input_password=request.POST['input_password']
        user=request.user.password
        print('입력:', input_password)
        print('비번:', user)
        if check_password(input_password, user):
            request.user.delete()
            logout(request)
            return render(request, 'login.html')

    return render(request, 'home.html')

class KakaoException(Exception):
      pass

def kakao_login(request):
    #이후 env 파일에 추가 필요
    rest_api_key= "6fec2af22db6826a94eba707eac15af5"
    #이후 도메인에 따른 수정 필요
    callback_url='http://127.0.0.1:8000/account/login/kakao/callback/'
    redirect_url= f"kauth.kakao.com/oauth/authorize?client_id={rest_api_key}&redirect_uri={callback_url}&response_type=code"
    return redirect(f"https://{redirect_url}")

def kakao_callback(request):
    try: 	
        rest_api_key= "6fec2af22db6826a94eba707eac15af5"
        callback_url='http://127.0.0.1:8000/account/login/kakao/callback/'
        code=request.GET.get("code")
            
        token_request= requests.get(
            f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={rest_api_key}&redirect_uri={callback_url}&code={code}"
        )
        token_response_json=token_request.json()
        error=token_response_json.get("error",None)
        # print(f"token_response_json : {token_response_json}")

        if error is not None:
            raise KakaoException("can not import kakao authorization code.")

        access_token=token_response_json.get("access_token")
        profile_request=requests.get(
            "https://kapi.kakao.com/v2/user/me",
            headers={"Authorization": f"Bearer {access_token}"}
        )
        profile_json=profile_request.json()

        # print(f"Profile : {profile_json}")
        try:
            user=user_models.User.objects.get(email=profile_json.get("kakao_account").get("email"))
        except:
            user=user_models.User.objects.create(
                email=profile_json.get("kakao_account").get("email")
            )
            user.set_unusable_password()
            user.save()

        login(request,user)

        return render(request, 'home.html')
    except KakaoException as error:
        return redirect("account:signup")
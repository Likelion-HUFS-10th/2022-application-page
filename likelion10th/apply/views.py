from django.shortcuts import render, redirect
from .models import Apply
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required(login_url='/account/login/')
def create(request):
    if Apply.objects.filter(user=request.user).exists():
        return redirect('apply:mydetail')  # 작성한 폼이 존재할 경우, detail or update 페이지로 넘어갑니다.
    if request.method == 'POST':   # 지원폼 작성 후 저장
        new_application = Apply()
        new_application.user = request.user   # user name
        new_application.category = request.POST['category']   # category
        new_application.study_url = request.POST['study_url']   # 깃헙 / 블로그 주소
        new_application.first_q = request.POST['q1']   # 질문 1
        new_application.second_q = request.POST['q2']   # 질문 2
        new_application.third_q = request.POST['q3']   # 질문 3
        new_application.fourth_q = request.POST['q4']   # 질문 4
        new_application.save()
        return redirect('apply:mydetail')
    return render(request, 'create.html')   # 로그인이 되어 있고 작성한 폼이 존재하지 않는 경우, create 페이지로 넘어갑니다.


def update(request):
    try:
        application = Apply.objects.get(user=request.user)
        if request.method == 'POST' and application.is_submitted == False:
            application.category = request.POST['category']   # category
            application.study_url = request.POST['study_url']   # 깃헙 / 블로그 주소
            application.first_q = request.POST['q1']   # 질문 1
            application.second_q = request.POST['q2']   # 질문 2
            application.third_q = request.POST['q3']   # 질문 3
            application.fourth_q = request.POST['q4']   # 질문 4
            application.save()
            return redirect('apply:mydetail')   # detail 페이지로 수정해야 함
        return render(request, 'update.html', {'apply': application})
    except Apply.DoesNotExist:
        return redirect('apply:create')

@login_required(login_url='/account/login/')
def mydetail(request):
    try: 
        apply = Apply.objects.get(user = request.user)
        return render(request, 'mydetail.html', {'apply':apply})
    except Apply.DoesNotExist:
        return redirect('apply:create')

@login_required(login_url='/account/login/')
def submit(request):
    application = Apply.objects.get(user = request.user)
    application.is_submitted = True
    application.save()
    return redirect('home')
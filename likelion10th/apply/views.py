from django.shortcuts import render, redirect
from .models import Apply
from account.models import User
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def create(request):
    if request.method == 'POST':
        new_application = Apply()
        form = AuthenticationForm(request=request, data=request.POST)
        username = form.cleaned_data.get('username')
        user = User().objects.filter(username=username)
        new_application.user = user.name    # user
        new_application.category = request.POST['category']   # category
        new_application.study_url = request.POST['study_url']   # 깃헙 / 블로그 주소
        new_application.first_q = request.POST['q1']   # 질문 1
        new_application.second_q = request.POST['q2']   # 질문 2
        new_application.third_q = request.POST['q3']   # 질문 3
        new_application.fourth_q = request.POST['q4']   # 질문 4
        new_application.save()
        return render(request, 'detail.html')   # detail 페이지로
    return render(request, 'create.html')

def update(request, id):
    form = Apply.objects.get(id=id)
    if request.method == 'POST':
        # form.user = ?
        form.category = request.POST['category']   # category
        form.study_url = request.POST['study_url']   # 깃헙 / 블로그 주소
        form.first_q = request.POST['q1']   # 질문 1
        form.second_q = request.POST['q2']   # 질문 2
        form.third_q = request.POST['q3']   # 질문 3
        form.fourth_q = request.POST['q4']   # 질문 4
        form.save()
        return redirect('apply:detail', form.id)
    return render(request, 'update.html', {'apply': form})
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Apply

# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required
def mydetail(request):
    apply = Apply.objects.get(user = request.user)
    print("apply : ", apply)
    print("user : ", request.user.name)
    return render(request, 'mydetail.html', {'apply':apply})
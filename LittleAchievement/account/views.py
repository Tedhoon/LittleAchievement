from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib import auth
from django import forms 
from .forms import RegisterForm, LoginForm
from task.models import CommonTask,MyTask
# Create your views here.
def index(request):
    context = dict()
    active_user = request.user
    context['all_common_task'] = CommonTask.objects.all()

    if str(active_user) != "AnonymousUser":

        context['all_my_task'] = MyTask.objects.filter(user = active_user, is_checked = False)
        context['total_task'] = MyTask.objects.filter(user = active_user).count()
        context['complete_task'] = MyTask.objects.filter(user = active_user, is_checked = True).count()
    return render(request, 'index.html',context)

def signup(request):
    if request.method =="POST":
        registerform = RegisterForm(request.POST)
        if registerform.is_valid():
            user_instance = registerform.save(commit=False)
            user_instance.set_password(registerform.cleaned_data['password1'])
            user_instance.is_active = True
            user_instance.save()
            user=User.objects.get(username=registerform.cleaned_data['username'])
            return redirect('index')
        else:
            registerform = RegisterForm(request.POST)
            return render(request, 'signup.html', {'RegisterForm' : registerform})
        
    registerform = RegisterForm()
    return render(request, 'signup.html', {'RegisterForm': registerform})

class LoginView(LoginView):
    template_name = 'registration/login.html' 
    authentication_form = LoginForm

def login(request):
    return render(request, 'login.html')
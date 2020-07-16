from django.shortcuts import render,redirect
from .models import CommonTask,MyTask
# Create your views here.
def subscribe(request):
    
    target_task = CommonTask.objects.get(id=request.POST.get('subscribe_task'))
    
    print(target_task)
    MyTask.objects.create(user= request.user, task = target_task)
    
    return redirect('index')
from django.shortcuts import render,redirect
from .models import CommonTask,MyTask
# Create your views here.
def subscribe(request):
    active_user  = request.user
    target_task = CommonTask.objects.get(id=request.POST.get('subscribe_task'))
    
    print("현재 등록된 Task 갯수 ; ", MyTask.objects.filter(user=active_user).count())

    if MyTask.objects.filter(user=active_user).count() < 3 and not MyTask.objects.filter(user=active_user,task = target_task).exists():
        MyTask.objects.create(user= active_user, task = target_task)
        print("새로운 할일이 등록 되었습니다.")
    return redirect('index')

def unsubscribe(request):
    active_user  = request.user
    target_task = MyTask.objects.get(id=request.POST.get('unsubscribe_task'))
    
    if target_task.user == active_user:
        target_task.delete()
        print("할일이 삭제되었습니다.")

    print("현재 등록된 Task 갯수 ; ", MyTask.objects.filter(user=active_user).count())
    return redirect('index')
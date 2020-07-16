from django.shortcuts import render,redirect
from .models import CommonTask,MyTask
from account.models import DayLog
from datetime import date

# Create your views here.
def subscribe(request):
    active_user  = request.user
    target_task = CommonTask.objects.get(id=request.POST.get('subscribe_task'))
    
    print("현재 등록된 Task 갯수 ; ", MyTask.objects.filter(user=active_user).count())

    if MyTask.objects.filter(user=active_user).count() < 5 and not MyTask.objects.filter(user=active_user,task = target_task).exists():
        MyTask.objects.create(user= active_user, task = target_task)
        print("새로운 할일이 등록 되었습니다.")
    return redirect('index')

def task_managing(request):
    active_user  = request.user
    
    if request.POST.get('unsubscribe_task'):
        target_task = MyTask.objects.get(id=request.POST.get('unsubscribe_task'))
        if target_task.user == active_user:
            target_task.delete()
            print("할일이 삭제되었습니다.")
            
    if request.POST.get('checking_task'):
        checking_task = MyTask.objects.get(id=request.POST.get('checking_task'))
        if checking_task.user == active_user:
            checking_task.is_checked = True
            checking_task.save()
            
            temp_date = date.today()
            
            log_add_count = DayLog.objects.get(user = active_user, date = temp_date)
            log_add_count.count += 1 
            log_add_count.save()
            
            print("하나의 일을 달성 하셨군요! 수고하셨어요!!.")

    print("현재 등록된 Task 갯수 ; ", MyTask.objects.filter(user=active_user).count())
    return redirect('index')
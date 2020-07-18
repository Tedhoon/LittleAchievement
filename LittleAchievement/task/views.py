from django.shortcuts import render,redirect
from .models import CommonTask,MyTask
from account.models import DayLog,TotalLog
from datetime import date



def index(request):
    context = dict()
    active_user = request.user
    # context['all_common_task'] = CommonTask.objects.all()

    if str(active_user) != "AnonymousUser":
        context['all_my_task'] = MyTask.objects.filter(user = active_user, is_checked = False)
        context['total_task'] = MyTask.objects.filter(user = active_user).count()
        context['complete_task'] = MyTask.objects.filter(user = active_user, is_checked = True).count()
        
        return render(request, 'index.html',context)

    else:
        return redirect('login')

# Create your views here.
def subscribe(request):
    active_user  = request.user
    target_task = CommonTask.objects.get(id=request.POST.get('subscribe_task'))
    
    print("현재 등록된 Task 갯수 ; ", MyTask.objects.filter(user=active_user).count())

    if MyTask.objects.filter(user=active_user).count() < 5 and not MyTask.objects.filter(user=active_user,task = target_task).exists():
        MyTask.objects.create(user= active_user, task = target_task)
        print("새로운 할일이 등록 되었습니다.")
    return redirect('tasklist')

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

            total_log = TotalLog.objects.filter(user = active_user,contents = checking_task.task)

            if total_log.exists():
                total_log = total_log.first()
                total_log.count += 1
                total_log.save()
                print("지금까지", total_log, "<---- 를",total_log.count,"했습니다")
            else:
                TotalLog.objects.create(user = active_user,contents = checking_task.task ,count = 1)
                print("없어서 토탈 로그를 하나 만들었습니다")
            

    print("현재 등록된 Task 갯수 ; ", MyTask.objects.filter(user=active_user).count())
    return redirect('index')
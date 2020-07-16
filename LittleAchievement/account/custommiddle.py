from .models import DayLog
from datetime import date
from task.models import MyTask

class ChangeCheckingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        

    def __call__(self, request):
        active_user = request.user
        # view 호출되기 전
        # print("뷰가 호출되기전")
        if not DayLog.objects.filter(user = active_user, date = date.today()).exists():
            change_task_list = MyTask.objects.filter(user=active_user)
            for one_task in change_task_list:
                one_task.is_checked = False
                one_task.save()
                print("변경된 one_task",one_task)
            print("=====checking status change complete...!=====")
            
        response = self.get_response(request)

        # view 호출 된 후
        # print("뷰가 호출된후에")
        return response
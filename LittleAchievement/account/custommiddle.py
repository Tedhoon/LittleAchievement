from .models import DayLog
from datetime import date
from task.models import MyTask,CommonTask
from django.contrib.auth.models import User 


class ChangeCheckingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        

    def __call__(self, request):
        
        active_user = request.user
        
        if str(active_user) != "AnonymousUser":

            temp_date =date.today()
            # view 호출되기 전
            # print("뷰가 호출되기전")

            if not DayLog.objects.filter(user = active_user, date = temp_date).exists(): #만약에 DayLog가 없다는것은 오늘 처음 접속

                DayLog.objects.create(user = active_user, date = temp_date) #날짜가 바뀌면 오늘의 로그를 만들어주고

                task_list = [i.name for i in CommonTask.objects.filter(maker = User.objects.get(username="jang") ).order_by('?')[0:4]] #랜덤으로 섞어서 4개의 공통 mission을 가져온다.
                print(task_list)
                change_task_list = MyTask.objects.filter(user=active_user) #기존의 TaskList를 들고와서 하루가 지났으니 is_checked를 업데이트 해주도록 하자
                for one_task in change_task_list:  #하나하나 돌면서 update를 해주는데
                    
                    #만약 요일이 지났으면 지워줘야한다.
                    if (date.today()-one_task.created).days >= one_task.task.period:   #날짜간의 차이를 계산해서 만약 기간이 지났ㅇ면 삭제해주도록 하자.
                        print("요일을 다채웠으므로 삭제됩니다!",one_task)
                        one_task.delete()
                        
                    else:
                        if one_task.task.maker.is_superuser: #만약 작성자가 운영자라면
                            one_task.task = CommonTask.objects.get(name = task_list.pop()) #random으로 섞은 mission을 하나씩 업데이트 해주고 save
                        one_task.is_checked = False      #그리고 checked 는 초기화해주자.
                        one_task.save()
                        print("변경된 one_task",one_task)

                print("=====checking status change complete...!=====")
                
        response = self.get_response(request)

        # view 호출 된 후
        # print("뷰가 호출된후에")
        return response
from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic.list import ListView

from task.models import CommonTask,MyTask,DetailTaskList
from django.urls import reverse_lazy

from django.core.exceptions import PermissionDenied

from task.forms import DetailTaskListForm

# Create your views here.
class TaskCreate(CreateView):
    model = CommonTask
    fields = ['name','maker','desc','tags','period',"is_list"]
    template_name = 'taskcreate.html'
    success_url = reverse_lazy('tasklist')

    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_category'] = ['일상', '스포츠', '교육', '감사']
        context['period'] = range(1,31)
        return context

    def post(self, request, *args, **kwargs):
        
        super().post(request, *args, **kwargs)
        latest_task = CommonTask.objects.filter(maker=request.user).order_by("created").last()
        print(request.POST.get('is_list'),"=======집중해라집중===========")
        if request.POST.get('is_list') == "True":
            print(request.POST.get("period"),"반복횟수~~~~~~~~~~~~~~~~~~~@@@@@@")
            
            for i in range(int(request.POST.get("period"))):
                print(request.POST.get("tasklist"+str(i)))
                tmp_task = DetailTaskListForm({'root':latest_task, 'desc': request.POST.get("tasklist"+str(i))})
                if tmp_task.is_valid():
                    print("잘 살아 남았다")
                    tmp_task.save()



        return redirect('tasklist')

        
            
        

class TaskList(ListView):
    model = CommonTask
    # paginate_by = 50
    template_name = 'tasklist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_list'] = CommonTask.objects.all()
        mytask_qs_list  = MyTask.objects.filter(user = self.request.user)
        mytask_list = [i.task for i in mytask_qs_list]
        context['mytask_list'] = mytask_list
        if len(mytask_list) == 5:
            context['full_task'] = True

        return context

class TaskUpdate(UpdateView):
    model = CommonTask
    fields = ['name','maker','desc','tags','period',"is_list"]
    template_name = 'taskupdate.html'
    success_url = reverse_lazy('tasklist')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.object.maker == self.request.user:
            return super().get(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def post(self, request, *args, **kwargs):
        
        super().post(request, *args, **kwargs)
        latest_task = CommonTask.objects.filter(maker=request.user).order_by("created").last()
        print(request.POST.get('is_list'),"=======집중해라집중===========")
        if request.POST.get('is_list') == "True":
            print(request.POST.get("period"),"반복횟수~~~~~~~~~~~~~~~~~~~@@@@@@")
            
            for i in range(int(request.POST.get("period"))):
                print(request.POST.get("tasklist"+str(i)))
                tmp_task = DetailTaskListForm({'root':latest_task, 'desc': request.POST.get("tasklist"+str(i))})
                if tmp_task.is_valid():
                    print("잘 살아 남았다")
                    tmp_task.save()



        return redirect('tasklist')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = self.get_object()
        
        context['task_category'] = ['일상', '스포츠', '교육', '감사']
        context['period'] = range(1,31)

        return context




def taskdelete(request,pk):
    del_task = CommonTask.objects.get(id = pk)
    if del_task.maker == request.user:
        del_task.delete()
        return redirect('tasklist')

    else:
        raise PermissionDenied

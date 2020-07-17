from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic.list import ListView

from task.models import CommonTask
from django.urls import reverse_lazy

from django.core.exceptions import PermissionDenied

# Create your views here.
class TaskCreate(CreateView):
    model = CommonTask
    fields = ['name','maker']
    template_name = 'taskcreate.html'
    success_url = reverse_lazy('tasklist')

class TaskList(ListView):
    model = CommonTask
    # paginate_by = 50
    template_name = 'tasklist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_list'] = CommonTask.objects.all()
        return context

class TaskUpdate(UpdateView):
    model = CommonTask
    fields = ['name','maker']
    template_name = 'taskupdate.html'
    success_url = reverse_lazy('tasklist')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.object.maker == self.request.user:
            return super().get(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = self.get_object()
        return context
    

def taskdelete(request,pk):
    del_task = CommonTask.objects.get(id = pk)
    if del_task.maker == request.user:
        del_task.delete()
        return redirect('tasklist')

    else:
        raise PermissionDenied

from django.urls import path
from .views import TaskCreate,TaskList,TaskUpdate,taskdelete
urlpatterns = [
    path('create/', TaskCreate.as_view(), name="taskcreate"),
    path('list/', TaskList.as_view(), name="tasklist"),
    path('update/<int:pk>', TaskUpdate.as_view(), name="taskupdate"),
    path('delete/<int:pk>', taskdelete, name="taskdelete"),

]

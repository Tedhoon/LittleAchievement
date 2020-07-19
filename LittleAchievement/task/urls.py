from django.urls import path
from .views import subscribe,task_managing
urlpatterns = [
    
    path('subscribe/', subscribe, name="subscribe"),
    path('task_managing/', task_managing, name="task_managing"),

]

from django.contrib import admin
from .models import CommonTask,MyTask
# Register your models here.
admin.site.register(CommonTask)
admin.site.register(MyTask)
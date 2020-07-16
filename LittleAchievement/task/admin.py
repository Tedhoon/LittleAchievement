from django.contrib import admin
from .models import CommonTask,CustomTask,MyTask
# Register your models here.
admin.site.register(CommonTask)
admin.site.register(CustomTask)
admin.site.register(MyTask)
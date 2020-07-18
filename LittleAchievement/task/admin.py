from django.contrib import admin
from .models import CommonTask,MyTask,DetailTaskList

# Register your models here.

class CommonTaskAdmin(admin.ModelAdmin):
    list_display = ['maker', 'name','tags','period','is_list','created']

class MyTaskAdmin(admin.ModelAdmin):
    list_display = ['user', 'task','created','is_checked'] 

class DetailTaskListAdmin(admin.ModelAdmin):
    list_display = ['root','desc'] 

admin.site.register(CommonTask,CommonTaskAdmin)
admin.site.register(MyTask,MyTaskAdmin)
admin.site.register(DetailTaskList,DetailTaskListAdmin)
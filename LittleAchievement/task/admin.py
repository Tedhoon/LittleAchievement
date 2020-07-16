from django.contrib import admin
from .models import CommonTask,MyTask
# Register your models here.

class CommonTaskAdmin(admin.ModelAdmin):
    list_display = ['maker', 'name','created']

class MyTaskAdmin(admin.ModelAdmin):
    list_display = ['user', 'task','created'] 
admin.site.register(CommonTask,CommonTaskAdmin)
admin.site.register(MyTask,MyTaskAdmin)
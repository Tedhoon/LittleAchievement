from django.contrib import admin
from .models import DayLog,TotalLog
# Register your models here.
class DayLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'date','count'] 

class TotalLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'contents','count'] 
admin.site.register(DayLog,DayLogAdmin)

admin.site.register(TotalLog,TotalLogAdmin)
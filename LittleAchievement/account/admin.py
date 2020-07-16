from django.contrib import admin
from .models import DayLog
# Register your models here.
class DayLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'date','count'] 

admin.site.register(DayLog,DayLogAdmin)
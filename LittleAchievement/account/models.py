from django.db import models
from django.conf import settings
from datetime import date
# Create your models here.

# class Profile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     username = models.CharField('별명', max_length=10)
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from task.models import CommonTask,MyTask
@receiver(post_save, sender=User)
def create_common_task(sender, instance, created, **kwargs):
    if created:
        task_list = CommonTask.objects.filter(maker = User.objects.get(username="myungsu") ).order_by('?')[0:4]
        for one_task in task_list:
            MyTask.objects.create(user=instance,task=one_task)
    
        

class DayLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE )
    date = models.DateField('날짜', default=date.today)
    count = models.PositiveIntegerField('성취',default = 0)

    def __str__(self):
        return str(self.date) 

class TotalLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE )
    contents = models.CharField("할 일", max_length=100)
    count = models.PositiveIntegerField('성취',default = 0)

    def __str__(self):
        return self.contents

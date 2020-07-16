from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class CommonTask(models.Model):
    maker = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_DEFAULT , default ="전학간 친구에요")  #탈퇴한 사용자꺼 보존
    name = models.CharField("할 일", max_length=100)
    created = models.DateTimeField(editable=False, default=timezone.now)

    def __str__(self):
        return self.name    

class MyTask(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE )
    task = models.ForeignKey(CommonTask,on_delete=models.CASCADE )  #탈퇴한 사용자꺼 보존
    created = models.DateTimeField(editable=False, default=timezone.now)

    def __str__(self):
        return str(self.task) 


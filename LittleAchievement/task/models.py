from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import date

# Create your models here.

class CommonTask(models.Model):
    maker = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_DEFAULT , default ="전학간 친구에요")  #탈퇴한 사용자꺼 보존
    name = models.CharField("할 일", max_length=100)
    desc = models.TextField("설명",blank = True,default="")
    tags = models.CharField('태그', max_length=200, default="일상")
    period = models.PositiveIntegerField("기간", default = 1)
    is_list = models.CharField("리스트여부", max_length=10 ,default="False",blank=True )
    image = models.ImageField('이미지', default="None")
    created = models.DateTimeField(editable=False, default=timezone.now)


    def __str__(self):
        return self.name    

class DetailTaskList(models.Model):
    root = models.ForeignKey(CommonTask, on_delete=models.CASCADE ) 
    desc = models.TextField("할 일")
    def __str__(self):
        return self.desc   

class MyTask(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE )
    task = models.ForeignKey(CommonTask,on_delete=models.CASCADE )  #탈퇴한 사용자꺼 보존

    is_checked = models.BooleanField('한번 해봐요', default=False)
    created = models.DateField("생성일",default=date.today)

    def __str__(self):
        return str(self.task) 


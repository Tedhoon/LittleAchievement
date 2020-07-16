from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class CommonTask(models.Model):
    name = models.CharField("할 일", max_length=100)
    created = models.DateTimeField(editable=False, default=timezone.now)

    def __str__(self):
        return self.name    
class CustomTask(CommonTask):
    maker = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_DEFAULT , default ="전학간 친구에요")  #탈퇴한 사용자꺼 보존하자

   
class MyTask(CustomTask):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE )

    


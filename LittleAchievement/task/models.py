from django.db import models

# Create your models here.
class CommonTask(models.Model):
    name = models.CharField("할 일", max_length=100)

class CustomTask(CommonTask):
    # maker = models.ForeignKey(유저모델)
    
    #생성자
class MyTask(CustomTask):
    #체크
    pass


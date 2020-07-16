from django.db import models
from django.conf import settings
from datetime import date
# Create your models here.

# class Profile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     username = models.CharField('별명', max_length=10)


class DayLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE )
    date = models.DateField('날짜', default=date.today)
    count = models.PositiveIntegerField('성취')

    def __str__(self):
        return self.date 

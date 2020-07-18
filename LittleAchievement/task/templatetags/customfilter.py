from django import template
from ..models import MyTask
from datetime import date

register = template.Library()

# 템플릿 태그 중복 제거하기 태그
@register.filter
def dayTask(inst):
    if inst.task.detailtasklist_set.all():
        order_list = [i for i in inst.task.detailtasklist_set.all().order_by('id')]
        print(order_list[(date.today()-inst.created).days])
    return order_list[(date.today()-inst.created).days]


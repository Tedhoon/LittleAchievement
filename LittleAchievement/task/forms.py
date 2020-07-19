from django.forms import ModelForm
from .models import DetailTaskList

class DetailTaskListForm(ModelForm):
    class Meta:
        model = DetailTaskList
        fields = ('root','desc')
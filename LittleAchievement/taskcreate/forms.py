from django.forms import ModelForm
from task.models import CommonTask

class CommonTaskForm(ModelForm):

    class Meta:
        model = CommonTask
        fields = ('name','maker','desc','tags','period',"is_list")
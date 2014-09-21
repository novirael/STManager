from django.forms import ModelForm, Textarea
from projects.models import Project
from tasks.models import Task


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'finish_date', 'sum_hours_work']

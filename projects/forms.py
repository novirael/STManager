from django.forms import ModelForm
from projects.models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            'name',
            'description',
            'finish_date',
            'sum_hours_work',
            'link_repository'
        ]

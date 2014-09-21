from django.forms import ModelForm, Textarea
from tasks.models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'time', 'project']
        widgets = {
            'name': Textarea(attrs={'cols': 8, 'rows': 1}),
            'description': Textarea(attrs={'cols': 8, 'rows': 1, 'placeholder': 'dupa'}),
            'time': Textarea(attrs={'cols': 8, 'rows': 1}),
        }

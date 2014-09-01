from django.views.generic import TemplateView
from tasks.models import Task


class TasksIndex(TemplateView):
    template_name = 'tasks/index.html'

    def get_context_data(self, **kwargs):
        context = super(TasksIndex, self).get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context

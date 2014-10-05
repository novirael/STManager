from django.views.generic import TemplateView, FormView
from django.core.urlresolvers import reverse_lazy

from projects.models import Project
from tasks.models import Task
from tasks.forms import TaskForm


class TasksIndex(TemplateView):
    template_name = 'tasks/index.html'

    def get_context_data(self, **kwargs):
        context = super(TasksIndex, self).get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context


class AddTask(FormView):
    template_name = 'tasks/add.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasks_app:index')

    def get_context_data(self, **kwargs):
        context = super(AddTask, self).get_context_data(**kwargs)
        context['project'] = Project.objects.all().values()
        return context

    def form_valid(self, form):
        form.save()
        return super(AddTask, self).form_valid(form)

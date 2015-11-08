from datetime import datetime
from django.views.generic import TemplateView, FormView, RedirectView
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


class TaskDetails(TemplateView):
    template_name = 'tasks/details.html'

    def get_context_data(self, **kwargs):
        context = super(TaskDetails, self).get_context_data(**kwargs)
        context['task'] = Task.objects.get(id=kwargs['id'])
        return context


class TaskCreate(FormView):
    template_name = 'tasks/create.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasks_app:index')

    def get_context_data(self, **kwargs):
        context = super(TaskCreate, self).get_context_data(**kwargs)
        context['project'] = Project.objects.all().values()
        return context

    def form_valid(self, form):
        form.save()
        return super(TaskCreate, self).form_valid(form)


class StartTask(RedirectView):
    permanent = False
    query_string = True
    url = reverse_lazy('tasks_app:index')

    def dispatch(self, request, *args, **kwargs):
        task = Task.objects.get(id=kwargs['id'])
        task.start_time = datetime.now()
        task.save()
        return super(StartTask, self).dispatch(request, *args, **kwargs)


class StopTask(RedirectView):
    permanent = False
    query_string = True
    url = reverse_lazy('tasks_app:index')

    def dispatch(self, request, *args, **kwargs):
        task = Task.objects.get(id=kwargs['id'])
        time_stop = datetime.now()
        delta = time_stop - task.start_time
        task.time += int(delta.total_seconds())
        task.start_time = None
        task.save()
        return super(StopTask, self).dispatch(request, *args, **kwargs)

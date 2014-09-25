from datetime import datetime, time
from django.views.generic import TemplateView, FormView, RedirectView
from tasks.forms import TaskForm
from tasks.models import Task


class TasksIndex(TemplateView):
    template_name = 'tasks/index.html'

    def get_context_data(self, **kwargs):
        context = super(TasksIndex, self).get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context


class AddTask(FormView):
    template_name = 'tasks/add.html'
    form_class = TaskForm

    def form_valid(self, form):
        form.save()
        return super(AddTask, self).form_valid(form)

    def get_success_url(self):
        return "/tasks"


class StartTask(RedirectView):
    permanent = False
    url = "/tasks"

    def dispatch(self, request, *args, **kwargs):
        task = Task.objects.get(id=kwargs['id'])
        task.start_time = datetime.now()
        task.save()
        return super(StartTask, self).dispatch(request, *args, **kwargs)


class StopTask(RedirectView):
    url = '/tasks'
    permanent = False

    def dispatch(self, request, *args, **kwargs):
        task = Task.objects.get(id=kwargs['id'])
        time_stop = datetime.now()
        delta = time_stop - task.start_time
        task.time += int(delta.total_seconds())
        task.start_time = None
        task.save()
        return super(StopTask, self).dispatch(request, *args, **kwargs)

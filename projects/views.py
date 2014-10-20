from django.views.generic import TemplateView, FormView
from django.core.urlresolvers import reverse_lazy

from projects.models import Project
from projects.forms import ProjectForm
from projects.utils import total_work_time_project
from tasks.models import Task


class AllProjectView(TemplateView):
    template_name = 'projects/index.html'

    def get_context_data(self, **kwargs):
        context = super(AllProjectView, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        return context


class AddProject(FormView):
    template_name = 'projects/add.html'
    form_class = ProjectForm
    success_url = reverse_lazy('projects_app:index')

    def form_valid(self, form):
        form.save()
        return super(AddProject, self).form_valid(form)


class ProjectDetails(TemplateView):
    template_name = 'projects/details.html'


    def get_context_data(self, **kwargs):
        context = super(ProjectDetails, self).get_context_data(**kwargs)
        tasks = Task.objects.filter(project_id=kwargs['id'])
        context['project'] = Project.objects.get(id=kwargs['id'])
        context['tasks'] = tasks
        context['time'] = total_work_time_project(tasks)
        return context

from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from projects.forms import ProjectForm
from projects.models import Project
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

    def form_valid(self, form):
        form.save()
        return super(AddProject, self).form_valid(form)

    def get_success_url(self):
        return "/projects"


class ProjectDetails(TemplateView):
    template_name = 'projects/details.html'

    def total_work_time_project(self, tasks):
        time = 0
        for task in tasks:
            time += task.time
        return time

    def get_context_data(self, **kwargs):
        context = super(ProjectDetails, self).get_context_data(**kwargs)
        context['tasks'] = Task.objects.filter(project_id=kwargs['id'])
        context['project'] = Project.objects.get(id=kwargs['id'])
        context['time'] = self.total_work_time_project(context['tasks'])
        return context


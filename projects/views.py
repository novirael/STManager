from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from projects.forms import ProjectForm
from projects.models import Project


class ProjectView(TemplateView):
    template_name = 'projects/index.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectView, self).get_context_data(**kwargs)
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
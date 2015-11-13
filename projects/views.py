from django.http import Http404

from django.views.generic import TemplateView, FormView, RedirectView
from django.core.urlresolvers import reverse_lazy

from projects.models import Project, NotSetTrelloBoardID
from projects.forms import ProjectForm


class ProjectIndex(TemplateView):
    template_name = 'projects/index.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectIndex, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        return context


class ProjectDetails(TemplateView):
    template_name = 'projects/details.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectDetails, self).get_context_data(**kwargs)
        project = Project.objects.get(id=kwargs['id'])
        context['project'] = project
        context['tasks'] = project.tasks.all()
        return context


class ProjectCreate(FormView):
    template_name = 'projects/create.html'
    form_class = ProjectForm
    success_url = reverse_lazy('projects_app:index')

    def form_valid(self, form):
        form.save()
        return super(ProjectCreate, self).form_valid(form)


class SyncWithTrello(RedirectView):
    permanent = False
    query_string = True,

    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('projects_app:details', kwargs={
            "id": kwargs['id']
        })

    def dispatch(self, request, *args, **kwargs):
        try:
            bms = Project.objects.get(id=kwargs['id'])
            bms.sync_trello_cards()
        except (Project.DoesNotExist, NotSetTrelloBoardID):
            raise Http404

        return super(SyncWithTrello, self).dispatch(request, *args, **kwargs)

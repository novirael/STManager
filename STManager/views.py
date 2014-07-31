from django.views.generic import DetailView


class Home(DetailView):
    template_name = 'templates/home.html'

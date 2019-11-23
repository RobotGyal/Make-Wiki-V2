from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from wiki.models import Page

class LoginView(ListView):
    model = Page

    def get(self, request):
        """ GET a list of Pages. """
        # pages = self.get_queryset().all()
        return render(request, 'login.html', {
        })

class SignUpView(ListView):
    model = Page

    def get(self, request):
        """ GET a list of Pages. """
        # pages = self.get_queryset().all()
        return render(request, 'signup.html', {
        })


class PageListView(ListView):
    """ Renders a list of all Pages. """
    model = Page

    def get(self, request):
        """ GET a list of Pages. """
        pages = self.get_queryset().all()
        return render(request, 'list.html', {
          'pages': pages
        })

class PageDetailView(DetailView):
    """ Renders a specific page based on it's slug."""
    model = Page

    def get(self, request, slug):
        """ Returns a specific wiki page by slug. """
        page = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'page.html', {
          'page': page
        })

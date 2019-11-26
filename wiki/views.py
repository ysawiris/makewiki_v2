from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from wiki.forms import PageForm
from django.urls import reverse_lazy
from wiki.models import Page


class PageListView(ListView):
    """ Renders a list of all Pages. """
    model = Page

    def get(self, request):
        """ GET a list of Pages. """
        pages = self.get_queryset().all()
        return render(request, 'list.html', {'pages': pages})

class PageDetailView(DetailView):
    """ Renders a specific page based on it's slug."""
    model = Page

    def get(self, request, slug):
        """ Returns a specific wiki page by slug. """
        page = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'page.html', {'page': page})

class PageCreateNewView(CreateView):
  def get(self, request):
    content = {'form': PageForm()}
    return render(request, 'create_new.html', content)
  
  def post(self, request):
    form = PageForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse_lazy('wiki-list-page'))
    return render(request, 'create_new.html', {'form': form})
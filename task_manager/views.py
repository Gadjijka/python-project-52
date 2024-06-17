from django.views.generic import (TemplateView, CreateView,
                                  UpdateView, DeleteView,
                                  ListView)


class IndexView(TemplateView):
    template_name = 'index.html'


class CustomCreateView(CreateView):
    pass


class CustomUpdateView(UpdateView):
    pass


class CustomDeleteView(DeleteView):
    pass


class CustomListView(ListView):
    pass

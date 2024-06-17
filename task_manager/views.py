from django.views.generic import (TemplateView, CreateView,
                                  UpdateView, DeleteView)


class IndexView(TemplateView):
    template_name = 'index.html'


class CustomCreateView(CreateView):
    pass


class CustomUpdateView(UpdateView):
    pass


class CustomDeleteView(DeleteView):
    pass

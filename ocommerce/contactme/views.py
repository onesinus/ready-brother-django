from django.views.generic.list import ListView

from .models import ContactMe


class ContactMeListView(ListView):
    model = ContactMe

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = ContactMe.objects.all()
        return context

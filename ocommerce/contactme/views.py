from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from .models import ContactMe


class ContactMeListView(ListView):
    model = ContactMe

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = ContactMe.objects.all()
        return context


class ContactMeCreateView(CreateView):
    model = ContactMe
    fields = ['name', 'email', 'phone_number', 'message']
    template_name = 'contactme/contactme_form.html'

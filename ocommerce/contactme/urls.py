from django.urls import path

from . import views

urlpatterns = [
    path('', views.ContactMeListView.as_view(), name='contactme-list'),
    path('create', views.ContactMeCreateView.as_view(), name="contactme-create"),
    path('update/(?P<pk>[0-9]+)/$', views.ContactMeUpdateView.as_view(), name="contactme-update"),
    path('delete/(?P<pk>[0-9]+)/$', views.ContactMeDeleteView.as_view(), name="contactme-delete"),
]

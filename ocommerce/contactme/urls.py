from django.urls import path

from . import views

urlpatterns = [
    path('', views.ContactMeListView.as_view(), name='contactme-list'),
    path('create', views.ContactMeCreateView.as_view(), name="contactme-create")
]

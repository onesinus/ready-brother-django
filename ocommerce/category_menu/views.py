from django.shortcuts import render
from .models import CategoryMenu


def show_category_menu(request):
    return render(request, "category_menu/list.html", {'category_menus': CategoryMenu.objects.all()})

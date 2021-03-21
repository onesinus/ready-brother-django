from django.shortcuts import render
from .models import Seller


def show_sellers(request):
    return render(request, "sellers/list.html", {'sellers': Seller.get_annotated_list()})

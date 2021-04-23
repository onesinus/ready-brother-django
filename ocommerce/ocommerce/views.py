from django.views.generic import TemplateView
from django.http import JsonResponse
from _helpers.memcached import MemcachedHelper

cache = MemcachedHelper()


class HomeView(TemplateView):
    template_name = 'common/home.html'


def try_set_memcached(request):
    cache.set_value('data_something', {'John': 'Doe'})
    return JsonResponse({"message": "key data_something has been set to memcached"})

def try_get_memcached(request):
    data_from_memcached = cache.get_value('data_something')
    return JsonResponse({"data_from_memcached": data_from_memcached})

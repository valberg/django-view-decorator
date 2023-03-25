from django.http import HttpResponse

from django_view_decorator import view


@view(paths="baz/", name="baz")
def baz_view(request):
    return HttpResponse("baz")

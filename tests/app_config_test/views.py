from django.http import HttpRequest
from django.http import HttpResponse

from .apps import view


@view(
    paths="testing/",
    name="testing",
)
def some_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse("testing")

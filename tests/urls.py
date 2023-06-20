from django.urls import path

from django_view_decorator import include_view_urls

urlpatterns = [
    path(
        "",
        include_view_urls(
            extra_modules=["tests.some_views"],
        ),
    ),
]

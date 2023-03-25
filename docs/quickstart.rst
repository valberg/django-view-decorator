Quickstart Guide
================

Here follows a step-by-step guide to get you started with **django-view-decorator**.


1. Install django-view-decorator
--------------------------------

Install django-view-decorator using pip::

    pip install django-view-decorator


2. Add ``django_view_decorator`` to your ``INSTALLED_APPS`` setting
-------------------------------------------------------------------

Add ``django_view_decorator`` to your ``INSTALLED_APPS`` setting::

    INSTALLED_APPS = (
        ...
        'django_view_decorator',
    )

3. Setup URL routing
--------------------

Add the following to your projects ``ROOT_URLCONF`` module::

    from django.urls import path

    from django_view_decorator import include_view_urls

    urlpatterns = [
        path("", include_view_urls()),
    ]

---------------------------------
4. Start using the view decorator
---------------------------------

Add the ``@view`` decorator to your views. Note that by default only views placed in the `views.py` module of you apps will be discovered::

    from django_view_decorator import view

    @view(
        paths="/my_view/",
        name="my_view",
    )
    def my_view(request):
        return HttpResponse("Hello World!")


    @view(
        paths="/login_required/",
        name="login_required",
        login_required=True,
    )
    def login_required_view(request):
        return HttpResponse("Hello World from behind the login!")


    @view(
        paths="/staff_required/",
        name="staff_required",
        staff_required=True,
    )
    def staff_required(request):
        return HttpResponse("Hello staff member!")


    @view(
        paths="/class_based_view/",
        name="class_based_view",
    )
    class MyView(View):
        def get(self, request):
            return HttpResponse("Hello World!")


5. Namespace your views
-----------------------

If you want to namespace your views, you can do so by adding the ``namespace`` argument to the ``@view`` decorator::

    @view(
        paths="/my_view/",
        name="my_view",
        namespace="my_namespace",
    )
    def my_view(request):
        return HttpResponse("Hello World!")

or you can even construct a view decorator with a namespace::

    from django_view_decorator import namespaced_decorator_factory


    namespaced_view = namespaced_decorator_factory(namespace="my_namespace")


    @namespaced_view(
        paths="/my_view/",
        name="my_view",
    )
    def my_view(request):
        return HttpResponse("Hello World!")

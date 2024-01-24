from collections.abc import Sequence
import importlib
import os

from django.urls import include
from django.urls import URLPattern
from django.urls import URLResolver


def include_view_urls(
    *,
    extra_modules: list[str] | None = None,
) -> tuple[Sequence[URLResolver | URLPattern], str | None, str | None]:
    """
    Include the view urls from the registry discovered by django_view_decorator, and
    optionally from the given modules.
    :param extra_modules: A list of modules to import before including the view urls.
    :return: A tuple of (urlpatterns, app_name, namespace) (result from calling
        include())
    """
    if extra_modules:
        for module in extra_modules:
            if module[0] == '/':
                module_files = [f[:-3] for f in os.listdir(module) if f.endswith(".py") and f != "__init__.py"]

                for module_name in module_files:
                    spec = importlib.util.spec_from_file_location(module_name, os.path.join(module, f"{module_name}.py"))
                    _module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(_module)
            else:
                importlib.import_module(f"{module}")

    return include("django_view_decorator.urls")

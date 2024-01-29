import importlib
import os
from collections.abc import Sequence

from django.urls import include
from django.urls import URLPattern
from django.urls import URLResolver


def include_view_urls(
    *,
    extra_modules: list[str] | None = None,
    extra_packages: list[str] | None = None,
) -> tuple[Sequence[URLResolver | URLPattern], str | None, str | None]:
    """
    Include the view urls from the registry discovered by django_view_decorator, and
    optionally from the given modules.
    :param extra_modules: A list of modules to import before including the view urls.
    :param extra_packages: A list of packages to import before including the view urls.
    :return: A tuple of (urlpatterns, app_name, namespace) (result from calling
        include())
    """
    if extra_modules:
        for module in extra_modules:
            importlib.import_module(f"{module}")

    if extra_packages:
        for package in extra_packages:
            if package[0] == "/":
                package_files = [
                    f[:-3]
                    for f in os.listdir(package)
                    if f.endswith(".py") and f != "__init__.py"
                ]

                for package_name in package_files:
                    spec = importlib.util.spec_from_file_location(
                        package_name,
                        os.path.join(package, f"{package_name}.py"),
                    )
                    spec.loader.exec_module(importlib.util.module_from_spec(spec))

    return include("django_view_decorator.urls")

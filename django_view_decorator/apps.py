import sys
from collections import defaultdict
from collections.abc import Callable
from dataclasses import dataclass
from typing import TypeAlias

# If python version is <= 3.10, use typing_extensions
if sys.version_info[1] > 10:
    from typing import TypeVarTuple
else:
    from typing_extensions import TypeVarTuple

from django.apps import AppConfig
from django.http import HttpRequest
from django.http import HttpResponse
from django.urls import path, URLPattern, include

from .conf import conf


ViewType: TypeAlias = Callable[[HttpRequest, TypeVarTuple], HttpResponse]


@dataclass(kw_only=True)
class View:
    paths: str | list[str]
    view: ViewType


class ViewRegistry:
    views: dict[str, dict[str, list[View]]] = {}

    @classmethod
    def register(
        cls,
        *,
        name: str,
        paths: str | list[str],
        view_func: ViewType,
        namespace: str | None = None,
    ) -> None:
        cls.views.setdefault(namespace, defaultdict(list))[name].append(
            View(paths=paths, view=view_func),
        )

    @classmethod
    def urlpatterns(cls) -> list[URLPattern]:
        urlpatterns = []
        for namespace, views in cls.views.items():
            _patterns = []
            for name, _views in views.items():
                for _view in _views:
                    if isinstance(_view.paths, str):
                        _patterns.append(
                            path(_view.paths, _view.view, name=name),
                        )
                    else:
                        for _path in _view.paths:
                            _patterns.append(
                                path(_path, _view.view, name=name),
                            )
            urlpatterns.append(
                path("", include((_patterns, namespace), namespace=namespace)),
            )

        return urlpatterns


class ViewDecoratorAppConf(AppConfig):
    name = "django_view_decorator"
    verbose_name = "Django View Decorator"

    def ready(self) -> None:
        if conf.DJANGO_VIEW_DECORATOR_AUTODISCOVER_VIEWS:
            from django.utils.module_loading import autodiscover_modules

            autodiscover_modules("views")

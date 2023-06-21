from django.apps import AppConfig as DjangoAppConfig

from .decorators import namespaced_decorator_factory


class AppConfig(DjangoAppConfig):
    namespace: str | None = None
    base_path: str | None = None

    @classmethod
    def get_view_decorator(cls):
        return namespaced_decorator_factory(
            namespace=cls.get_namespace(),
            base_path=cls.get_base_path(),
        )

    @classmethod
    def get_namespace(cls):
        return cls.namespace or cls.name

    @classmethod
    def get_base_path(cls):
        return cls.base_path

from django.conf import settings


class Settings:
    @property
    def DJANGO_VIEW_DECORATOR_AUTODISCOVER_VIEWS(self) -> bool:
        return getattr(settings, "DJANGO_VIEW_UTILS_AUTODISCOVER_VIEWS", True)

    @property
    def DJANGO_VIEW_DECORATOR_AUTODISCOVER_MODULE(self) -> str:
        return getattr(settings, "DJANGO_VIEW_DECORATOR_AUTODISCOVER_MODULE", "views")


conf = Settings()

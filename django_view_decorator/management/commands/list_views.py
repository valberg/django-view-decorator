from django.core.management.base import BaseCommand

from django_view_decorator.apps import ViewRegistry


class Command(BaseCommand):
    help = "List all views in the project."

    def handle(self, *args, **options):
        for namespace, view in ViewRegistry.views.items():
            for name, views in view.items():
                for _view in views:
                    meta_data = (
                        f"name: {name}, view: "
                        f"{_view.view.__module__}.{_view.view.__name__}"
                    )
                    if isinstance(_view.paths, str):
                        self.stdout.write(f"{_view.paths} ({meta_data})")
                    else:
                        for path in _view.paths:
                            self.stdout.write(f"{path} ({meta_data})")

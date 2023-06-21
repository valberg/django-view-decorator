from django_view_decorator import AppConfig


class AppConfigTestAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tests.app_config_test"
    namespace = "app_config_test"
    base_path = "app-config-test"


view = AppConfigTestAppConfig.get_view_decorator()

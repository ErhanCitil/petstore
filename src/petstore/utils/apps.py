from django.apps import AppConfig


class UtilsConfig(AppConfig):
    name = "petstore.utils"

    def ready(self):
        from . import checks  # noqa

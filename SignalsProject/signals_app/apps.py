from django.apps import AppConfig


class SignalsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'signals_app'

    def ready(self) -> None:
        import signals_app.signals
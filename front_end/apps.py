from django.apps import AppConfig


class FrontEndConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'front_end'

    def ready(self):
        import front_end.signals

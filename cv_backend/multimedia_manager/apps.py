from django.apps import AppConfig


class MultimediaManagerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'multimedia_manager'

    def ready(self):
        import multimedia_manager.signals

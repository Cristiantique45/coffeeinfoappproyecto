from django.apps import AppConfig


class Modulo1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'modulo1'
    
    def ready(self):
        import modulo1.signals

from django.apps import AppConfig


class WebpageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Webpage'
    
    def ready(self):
     import Webpage.signals
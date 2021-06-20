from django.apps import AppConfig


class RestapiConfig(AppConfig):
    name = 'restapi'

    def ready(self):
        print('This is before the server run')

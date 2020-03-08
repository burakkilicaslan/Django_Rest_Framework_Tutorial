from django.apps import AppConfig
from actstream import registry


class CommunityConfig(AppConfig):
    name = 'community'

    def ready(self):
        registry.register(self.get_model('User'))
        registry.register(self.get_model('communities'))


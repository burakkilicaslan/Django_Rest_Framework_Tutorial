from django.apps import AppConfig
from actstream import registry
from django.contrib.auth.models import User
from community.models import communities


class CommunityConfig(AppConfig):
    name = 'community'

    def ready(self):
        registry.register(communities)
        registry.register(User)
        registry.register(self.get_model('post_type'))



from django.apps import AppConfig
from django.contrib.auth.models import User
from community.models import communities


class CommunityAppConfig(AppConfig):
    name = 'community'

    def ready(self):
        from actstream import registry
        registry.register(communities)
        registry.register(User)
        registry.register(self.get_model('post_type'))



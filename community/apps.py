from django.apps import AppConfig


class MyAppConfig(AppConfig):
    name = 'community'

    def ready(self):
        from django.contrib.auth.models import User
        from actstream import registry
        registry.register(self.get_model('communities'))
        registry.register(User)
        registry.register(self.get_model('post_type'))

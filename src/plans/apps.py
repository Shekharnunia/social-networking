from django.apps import AppConfig


class PlansConfig(AppConfig):
    name = 'plans'

    def ready(self):
        import plans.signals

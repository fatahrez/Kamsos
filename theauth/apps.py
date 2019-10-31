from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class TheauthConfig(AppConfig):
    name = 'theauth'
    verbose_name = _('profiles')

    def ready(self):
        import theauth.signals
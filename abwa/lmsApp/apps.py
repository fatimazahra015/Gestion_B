import importlib
import importlib.util

from django.apps import AppConfig


class lmsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lmsApp'

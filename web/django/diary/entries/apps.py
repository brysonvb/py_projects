""" App for diary """
from django.apps import AppConfig


class EntriesConfig(AppConfig):
    """ app configuration for diary """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'entries'

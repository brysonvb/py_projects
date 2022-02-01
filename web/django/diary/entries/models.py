"""Django Models - Diary Entries
"""
from django.db import models
from django.utils import timezone


class Entry(models.Model):
    """ Diary entry model """
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """ title of entry is retured when object string is queried """
        return str(self.title)

    class Meta: # pylint:disable=too-few-public-methods
        """ fix so that django uses Entries instead of Entrys """
        verbose_name_plural = "Entries"

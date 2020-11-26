from django.conf import settings
from django.db import models

class Organizer(models.Model):
    '''An Organizer is a User who manages Opportunities.'''
    user = models.OneToOneField(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
            primary_key=True
    )
    # TODO Opportunities

    def __str__(self):
        return f'Organizer {self.user}'

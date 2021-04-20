
from django.db import models


class Organization(models.Model):
    '''An Organization is a collection of organizers, joined via foreign key in the organizer model'''

    # Organization metadata
    name = models.TextField(help_text='Organization name')
    description = models.TextField(help_text='Organization description')
    website = models.TextField(help_text='Organization website')
    org_type = models.TextField(help_text='Organization type')

    def __str__(self):
        return f'Organization: {self.name}'

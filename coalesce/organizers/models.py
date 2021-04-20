from django.conf import settings
from django.db import models


class Organizer(models.Model):
    '''An Organizer is a User who manages Opportunities.'''
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True
    )

    organization = models.ForeignKey('organizations.Organization', on_delete=models.CASCADE, null=True)

    # The list of Opportunity objects that this Organizer manages is
    # 'opportunity_set'. It's the backwards ManyToMany relation for
    # Opportunity.organizers.

    def __str__(self):
        return f'Organizer {self.user}'

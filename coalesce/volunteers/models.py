from django.conf import settings
from django.db import models


class Volunteer(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True
    )
    description = models.TextField()
    # TODO List of Opportunities they have indicated interest in
    skills = models.TextField(help_text='List of skills the volunteer has')  # TODO is this just a string?
    organization = models.TextField(help_text='The volunteer\'s employer or organization')
    # TODO Background check date and document
    organizer_comments = models.TextField(help_text='Notes from organizers about this volunteer')

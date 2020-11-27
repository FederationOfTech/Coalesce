import uuid

from django.db import models

class Opportunity(models.Model):

    background_check_requirements = models.TextField()
    commitment_type = models.TextField()
    datetime = models.DateTimeField(auto_now=True, help_text="Event date")
    description = models.TextField()
    clothing_requirements = models.TextField()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # TODO image = models.ChartField(max_length=30)  # this should be ref to a stored image url
    location = models.TextField()
    # TODO organizer = models.ManyToManyRel()
    personnel_needed = models.TextField()
    post_privacy = models.CharField(choices=[
        ("public", "public"),
        ("private", "private"),
        ("unlisted", "unlisted"),
    ], default="public", max_length=8)
    skills_required = models.TextField()
    title = models.CharField(max_length=60)
    training_requirements = models.TextField()

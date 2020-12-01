from django.db import models
from django.contrib.postgres.fields import ArrayField

class Opportunity(models.Model):

    background_check_requirements = models.TextField()
    commitment_type = models.TextField()
    datetime = models.DateTimeField()
    description = models.TextField()
    clothing_requirements = models.TextField(blank=True)
    # TODO image = models.ChartField(max_length=30)  # this should be ref to a stored image url
    location = models.TextField()
    organizers = models.ManyToManyField('organizers.Organizer')
    personnel_needed = models.IntegerField()
    post_privacy = models.CharField(choices=[
        ("public", "public"),
        ("private", "private"),
        ("unlisted", "unlisted"),
    ], default="public", max_length=8)
    skills_required = ArrayField(models.CharField(max_length=60))
    title = models.CharField(max_length=60)
    # TODO training_requirements = models.TextField() # this should ref training data type

import uuid

from django.db import models

class Opportunity(models.Model):

    background_check_requirements = models.TextField()
    commitment_type = models.TextField() # should this have a constrained list?
    datetime = models.DateTimeField(auto_now=True, help_text="Event date") # What happens when this is a regular event?
    description = models.TextField()
    clothing_requirements = models.TextField()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # TODO image = models.ChartField(max_length=30) # this should be ref to a stored image url
    location = models.TextField() # is the geo-location, or virtual/non-virtual as stated in #6
    # TODO organizer = models.ManyToManyRel() # relationship with organiser
    personnel_needed = models.TextField() # should this is be a list of users?
    post_privacy = models.CharField(choices=[
        ("public", "public"),
        ("private", "private"),
        ("unlisted", "unlisted"),
    ], default="public", max_length=8)
    skills_required = models.TextField()  # should the be a list of some sort?
    title = models.CharField(max_length=60)
    training_requirements = models.TextField()  # should the be a list of some sort?

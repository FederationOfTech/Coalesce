from django.db import models

class Opportunity(models.Model):
    title = models.TextField()
    timestamp = models.DateTimeField()
    description = models.TextField()

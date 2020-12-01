import uuid

from django.db import models


class TrainingDetails(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(help_text='Name of the training')
    link = models.URLField(help_text='Link to online training course')
    date = models.DateField(help_text='Date of the training')

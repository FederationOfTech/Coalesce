from django.contrib import admin
from .models import Volunteer


@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    pass

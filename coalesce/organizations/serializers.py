from rest_framework import serializers
from .models import Organization
from ..organizers.models import Organizer

class OrganizationSerializer(serializers.ModelSerializer):
    organizers = serializers.PrimaryKeyRelatedField(
        queryset=Organizer.objects.all(),
        many=True
    )

    class Meta:
        model = Organization
        fields = ('id',
                  'name',
                  'description',
                  'website',
                  'org_type'
                  )

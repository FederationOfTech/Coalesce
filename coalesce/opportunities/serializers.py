from rest_framework import serializers
from .models import Opportunity
from ..organizers.models import Organizer

class OpportunitySerializer(serializers.ModelSerializer):
    organizers = serializers.PrimaryKeyRelatedField(
        queryset=Organizer.objects.all(),
        many=True
    )
    skills_required = serializers.ListField()

    class Meta:
        model = Opportunity
        fields = ('id',
                  'datetime',
                  'title',
                  'description',
                  'location',
                  'organizers',
                  'personnel_needed',
                  'skills_required',
                  'commitment_type',
                  'background_check_requirements',
                  # TODO 'image',
                  'clothing_requirements',
                  'post_privacy',
                  # TODO 'training_requirements'
                  )

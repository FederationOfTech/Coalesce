from rest_framework import serializers
from .models import Opportunity

class OpportunitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Opportunity
        fields = ('id', 'title', 'timestamp', 'description')


class CreateOpportunitySerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        opportunity = Opportunity.objects.create(**validated_data)
        return opportunity

    class Meta:
        model = Opportunity
        fields = ('title', 'timestamp', 'description')

from rest_framework import serializers
from .models import Volunteer

class CreateVolunteerSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Volunteer.objects.create(user=self.context['request'].user,
                                        **validated_data)

    class Meta:
        model = Volunteer
        fields = ('description', 'skills', 'organization', 'user',)
        read_only_fields = ('user',)

class VolunteerDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Volunteer
        fields = ('description', 'skills', 'organization', 'user',)

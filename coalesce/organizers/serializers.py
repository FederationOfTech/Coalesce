from rest_framework import serializers
from .models import Organizer


class CreateOrganizerSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Organizer.objects.create(user=self.context['request'].user,
                                        **validated_data)

    class Meta:
        model = Organizer
        fields = ('user', 'organization')
        read_only_fields = ('user',)

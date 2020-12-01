from rest_framework import serializers
from .models import TrainingDetails


class CreateTrainingDetailsSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return TrainingDetails.objects.create(**validated_data)

    class Meta:
        model = TrainingDetails
        fields = ('id', 'name', 'link', 'date',)


class TrainingDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingDetails
        fields = ('id', 'name', 'link', 'date',)

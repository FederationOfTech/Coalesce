from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from .models import TrainingDetails
from .serializers import TrainingDetailsSerializer, CreateTrainingDetailsSerializer


class TrainingDetailsCreateViewSet(mixins.CreateModelMixin,
                                   viewsets.GenericViewSet):
    queryset = TrainingDetails.objects.all()
    serializer_class = CreateTrainingDetailsSerializer
    permission_classes = (IsAuthenticated,)


class TrainingDetailsViewSet(mixins.RetrieveModelMixin,
                             viewsets.GenericViewSet):
    queryset = TrainingDetails.objects.all()
    serializer_class = TrainingDetailsSerializer
    permission_classes = (IsAuthenticated,)

from rest_framework import viewsets, mixins
from .models import Organizer
from rest_framework.permissions import IsAuthenticated
from .serializers import CreateOrganizerSerializer


class OrganizerCreateViewSet(mixins.CreateModelMixin,
                             viewsets.GenericViewSet):
    """
    Creates organizers
    """
    queryset = Organizer.objects.all()
    serializer_class = CreateOrganizerSerializer
    permission_classes = (IsAuthenticated,)

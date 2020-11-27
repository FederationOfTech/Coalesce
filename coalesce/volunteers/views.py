from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from .models import Volunteer
from .serializers import CreateVolunteerSerializer


class VolunteerCreateViewSet(mixins.CreateModelMixin,
                             viewsets.GenericViewSet):
    """
    Creates volunteers
    """
    queryset = Volunteer.objects.all()
    serializer_class = CreateVolunteerSerializer
    permission_classes = (IsAuthenticated,)

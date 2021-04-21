from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from .models import Organization
from .serializers import OrganizationSerializer


class OrganizationViewSet(mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.CreateModelMixin,
                          mixins.ListModelMixin,
                          viewsets.GenericViewSet):
    """
    Updates and retrieves opportunities.
    """
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = (AllowAny,)

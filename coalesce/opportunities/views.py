from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from rest_framework import filters

from .models import Opportunity
from .serializers import OpportunitySerializer


class OpportunityViewSet(mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    """
    Updates and retrieves opportunities.
    """
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer
    permission_classes = (AllowAny,)
    filter_backends = [filters.SearchFilter]
    search_fields = ["@title", "@description"]

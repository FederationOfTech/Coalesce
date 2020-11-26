from rest_framework import viewsets, mixins
from .models import Opportunity
from .serializers import OpportunitySerializer


class OpportunityViewSet(mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         viewsets.GenericViewSet):
    """
    Updates and retrieves opportunities.
    """
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer

from rest_framework import viewsets, mixins
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework import filters

from .models import Opportunity
from .serializers import OpportunitySerializer


class OpportunityOwnerPermission(BasePermission):
    """
    Only allow users who appear in the object organizers list to submit PATCH requests
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True

        # For updates, the user must be listed as an organizer of the opportunity
        return request.user in [o.user for o in obj.organizers.all()]

    def has_permission(self, request, view):
        # To post a new object simply test if the user is authenticated
        # TODO: Also verify that the user is an organizer
        if request.method == 'POST':
            return request.user.is_authenticated
        return True


class OpportunityViewSet(mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    """
    Retrieves opportunities.
    """
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["@title", "@description"]
    permission_classes = (OpportunityOwnerPermission,)

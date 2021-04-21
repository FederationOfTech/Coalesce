
import factory

from django.urls import reverse
from nose.tools import eq_
from rest_framework.test import APITestCase
from rest_framework import status
from ..models import Organization
from ...organizations.test.factories import OrganizationFactory


class TestOrganizationCreate(APITestCase):
    """
    Tests /organizers create operations.
    """

    def setUp(self):
        self.organization_data = factory.build(
            dict, FACTORY_CLASS=OrganizationFactory
        )
        self.url = reverse('organization-list')

    def test_post_request_with_valid_data_succeeds(self):
        response = self.client.post(self.url, self.organization_data)
        eq_(response.status_code, status.HTTP_201_CREATED)

        organization = Organization.objects.get(pk=response.data.get('id'))
        eq_(organization.name, self.organization_data.get('name'))

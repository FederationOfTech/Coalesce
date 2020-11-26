from django.urls import reverse
from nose.tools import ok_, eq_
from rest_framework.test import APITestCase
from rest_framework import status

import factory
from .factories import OpportunityFactory


class TestOpportunitiesListTestCase(APITestCase):
    """
    Tests /users list operations.
    """

    def setUp(self):
        self.url = reverse('opportunity-list')
        self.opportunity_data = factory.build(dict, FACTORY_CLASS=OpportunityFactory)

    def test_post_request_with_no_data_fails(self):
        response = self.client.post(self.url, {})
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

from django.urls import reverse
from nose.tools import eq_
from rest_framework.test import APITestCase
from rest_framework import status

import factory
from .factories import OpportunityFactory
from ..models import Opportunity


class TestOpportunitiesListTestCase(APITestCase):
    """
    Tests /opportunities list operations.
    """

    def setUp(self):
        self.url = reverse('opportunity-list')
        self.opportunity_data = factory.build(
            dict, FACTORY_CLASS=OpportunityFactory
        )

    def test_post_request_with_no_data_fails(self):
        response = self.client.post(self.url, {})
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_with_valid_data_succeeds(self):
        response = self.client.post(self.url, self.opportunity_data)
        eq_(response.status_code, status.HTTP_201_CREATED)

        opportunity = Opportunity.objects.get(pk=response.data.get('id'))
        eq_(opportunity.title, self.opportunity_data.get('title'))
        eq_(opportunity.description, self.opportunity_data.get('description'))


class TestOpportunityDetailTestCase(APITestCase):
    """
    Tests /opportunities detail operations.
    """

    def setUp(self):
        self.opportunity = OpportunityFactory()
        self.url = reverse('opportunity-detail', kwargs={'pk': self.opportunity.pk})

    def test_get_request_returns_a_given_opportunity(self):
        response = self.client.get(self.url)
        eq_(response.status_code, status.HTTP_200_OK)

    def test_patch_request_updates_an_opportunity(self):
        new_title = "New title"
        payload = {'title': new_title}
        response = self.client.patch(self.url, payload)
        eq_(response.status_code, status.HTTP_200_OK)

        opportunity = Opportunity.objects.get(pk=self.opportunity.id)
        eq_(opportunity.title, new_title)

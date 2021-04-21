from django.urls import reverse
from nose.tools import eq_
from rest_framework.test import APITestCase
from rest_framework import status

import factory
from .factories import OpportunityFactory
from ..models import Opportunity
from ...organizers.test.factories import OrganizerFactory
from ...users.test.factories import UserFactory


class TestOpportunitiesListTestCase(APITestCase):
    """
    Tests /opportunities list operations.
    """

    def setUp(self):
        self.url = reverse('opportunity-list')
        self.opportunity_data = factory.build(
            dict, FACTORY_CLASS=OpportunityFactory
        )
        self.user = UserFactory()

    def test_anonymous_post_request_fails(self):
        response = self.client.post(self.url, {})
        eq_(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_request_with_no_data_fails(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.user.auth_token}')
        response = self.client.post(self.url, {})
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_with_valid_data_succeeds(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.user.auth_token}')
        response = self.client.post(self.url, self.opportunity_data)
        eq_(response.status_code, status.HTTP_201_CREATED)

        opportunity = Opportunity.objects.get(pk=response.data.get('id'))
        eq_(opportunity.title, self.opportunity_data.get('title'))
        eq_(opportunity.description, self.opportunity_data.get('description'))

    def test_post_request_with_query_params_returns_subset(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.user.auth_token}')
        response = self.client.post(self.url, self.opportunity_data)
        eq_(response.status_code, status.HTTP_201_CREATED)

        opportunity = Opportunity.objects.get(pk=response.data.get('id'))
        eq_(opportunity.title, self.opportunity_data.get('title'))
        eq_(opportunity.description, self.opportunity_data.get('description'))

        search_url = self.url + "?search=test"
        response = self.client.get(search_url)

        eq_(1, len(response.data["results"]))
        opportunity = Opportunity.objects.get(pk=response.data["results"][0].get("id"))
        eq_(opportunity.title, self.opportunity_data.get('title'))
        eq_(opportunity.description, self.opportunity_data.get('description'))

        search_url = self.url + "?search=foo-no-results"
        response = self.client.get(search_url)
        eq_(0, len(response.data["results"]))


class TestOpportunityDetailTestCase(APITestCase):
    """
    Tests /opportunities detail operations.
    """

    def setUp(self):
        self.opportunity = OpportunityFactory()
        self.url = reverse('opportunity-detail', kwargs={'pk': self.opportunity.pk})

        # Creata an organizer and add them to the opportunity
        self.organizer = OrganizerFactory()
        self.opportunity.organizers.add(self.organizer)

    def test_get_request_returns_a_given_opportunity(self):
        response = self.client.get(self.url)
        eq_(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_patch_request_forbidden(self):
        new_title = "New title"
        payload = {'title': new_title}
        response = self.client.patch(self.url, payload)
        eq_(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_wrong_user_patch_request_forbidden(self):
        other_user = OrganizerFactory()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {other_user.user.auth_token}')
        new_title = "New title"
        payload = {'title': new_title}
        response = self.client.patch(self.url, payload)
        eq_(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_patch_request_updates_an_opportunity(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.organizer.user.auth_token}')
        new_title = "New title"
        payload = {'title': new_title}
        response = self.client.patch(self.url, payload)
        eq_(response.status_code, status.HTTP_200_OK)

        opportunity = Opportunity.objects.get(pk=self.opportunity.id)
        eq_(opportunity.title, new_title)

    def test_authenticated_patch_request_updates_organizers(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.organizer.user.auth_token}')
        new_organizer = OrganizerFactory()
        payload = {'organizers': [new_organizer.pk]}
        response = self.client.patch(self.url, payload)
        eq_(response.status_code, status.HTTP_200_OK)

        opportunity = Opportunity.objects.get(pk=self.opportunity.id)
        organizers = opportunity.organizers.all()
        eq_(organizers.count(), 1)
        eq_(str(organizers[0].pk), new_organizer.pk)

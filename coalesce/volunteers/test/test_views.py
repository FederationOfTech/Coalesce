from django.urls import reverse
from nose.tools import eq_
from rest_framework.test import APITestCase
from rest_framework import status
from ...users.test.factories import UserFactory
from .factories import VolunteerFactory
from ..models import Volunteer


class TestVolunteerCreate(APITestCase):
    """
    Tests /volunteers create operations.
    """

    def setUp(self):
        self.user = UserFactory()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.user.auth_token}')
        self.url = reverse('volunteer-list')
        self.user_data = {
            'description': 'I am a volunteer.',
            'skills': 'cooking, eating',
            'organization': 'Cambden Giving',
        }

    def test_post_request_with_no_data_fails(self):
        response = self.client.post(self.url, {})
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_with_valid_data_succeeds(self):
        response = self.client.post(self.url, self.user_data)
        eq_(response.status_code, status.HTTP_201_CREATED)

        volunteer = Volunteer.objects.get(pk=response.data.get('user'))
        eq_(str(response.data.get('user')), self.user.id)
        eq_(response.data.get('description'), volunteer.description)
        eq_(response.data.get('skills'), volunteer.skills)
        eq_(response.data.get('organization'), volunteer.organization)


class TestVolunteerDetails(APITestCase):
    """
    Tests /volunteers details operations.
    """

    def setUp(self):
        self.volunteer = VolunteerFactory()
        self.url = reverse('volunteer-detail', kwargs={'pk': self.volunteer.pk})

    def test_get_request_with_no_authorization_fails(self):
        response = self.client.get(self.url)
        eq_(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_request_with_authorization_succeeds(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.volunteer.user.auth_token}')
        response = self.client.get(self.url)
        eq_(response.status_code, status.HTTP_200_OK)
        eq_(str(response.data.get('user')), self.volunteer.user.id)
        eq_(response.data.get('description'), self.volunteer.description)
        eq_(response.data.get('skills'), self.volunteer.skills)
        eq_(response.data.get('organization'), self.volunteer.organization)

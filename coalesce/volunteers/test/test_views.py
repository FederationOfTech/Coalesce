from django.urls import reverse
from nose.tools import eq_
from rest_framework.test import APITestCase
from rest_framework import status
from ...users.test.factories import UserFactory
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

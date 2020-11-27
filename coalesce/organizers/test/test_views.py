from django.urls import reverse
from nose.tools import eq_
from rest_framework.test import APITestCase
from rest_framework import status
from ...users.test.factories import UserFactory


class TestOrganizerCreate(APITestCase):
    """
    Tests /organizers create operations.
    """

    def setUp(self):
        self.user = UserFactory()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.user.auth_token}')
        self.url = reverse('organizer-list')

    def test_post_request_with_valid_data_succeeds(self):
        response = self.client.post(self.url, {})
        eq_(response.status_code, status.HTTP_201_CREATED)

        eq_(str(response.data.get('user')), self.user.id)

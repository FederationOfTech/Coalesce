from django.urls import reverse
from nose.tools import eq_
from rest_framework.test import APITestCase
from rest_framework import status
from ...users.test.factories import UserFactory
from ..models import Organizer


class TestOrganizerCreate(APITestCase):
    """
    Tests /organizers create operations.
    """

    def setUp(self):
        self.user = UserFactory()
        self.url = reverse('organizer-list')

    def test_post_request_with_no_data_fails(self):
        response = self.client.post(self.url, {})
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_with_valid_data_succeeds(self):
        response = self.client.post(self.url, {'user': self.user.id})
        eq_(response.status_code, status.HTTP_201_CREATED)

        organizer = Organizer.objects.get(pk=response.data.get('user'))
        eq_(str(response.data.get('user')), self.user.id)

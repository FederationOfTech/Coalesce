import datetime
from django.urls import reverse
from nose.tools import eq_
from rest_framework.test import APITestCase
from rest_framework import status
from ...users.test.factories import UserFactory
from .factories import TrainingDetailsFactory
from ..models import TrainingDetails


class TestTrainingDetailsCreate(APITestCase):
    """
    Tests /training_details create operations
    """

    def setUp(self):
        self.user = UserFactory()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.user.auth_token}')
        self.url = reverse('trainingdetails-list')
        self.training_details_data = {
            'name': 'Test Training',
            'link': 'https://www.federationof.tech/',
            'date': datetime.date.fromisoformat('2020-11-27'),
        }

    def test_post_request_with_no_data_fails(self):
        response = self.client.post(self.url, {})
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_with_valid_data_succeeds(self):
        response = self.client.post(self.url, self.training_details_data)
        eq_(response.status_code, status.HTTP_201_CREATED)

        training_details = TrainingDetails.objects.get(pk=response.data.get('id'))
        eq_(response.data.get('id'), str(training_details.id))
        eq_(response.data.get('name'), training_details.name)
        eq_(response.data.get('link'), training_details.link)
        eq_(datetime.date.fromisoformat(response.data.get('date')), training_details.date)


class TestTrainingDetailsDetail(APITestCase):
    """
    Tests /training_details detail operations
    """

    def setUp(self):
        self.user = UserFactory()
        self.training_details = TrainingDetailsFactory()
        self.url = reverse('trainingdetails-detail', kwargs={'pk': self.training_details.pk})

    def test_get_request_with_no_authorization_fails(self):
        response = self.client.get(self.url)
        eq_(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_request_with_authorization_succeeds(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.user.auth_token}')
        response = self.client.get(self.url)
        eq_(response.status_code, status.HTTP_200_OK)
        eq_(response.data.get('id'), self.training_details.id)
        eq_(response.data.get('name'), self.training_details.name)
        eq_(response.data.get('link'), self.training_details.link)
        eq_(datetime.date.fromisoformat(response.data.get('date')), self.training_details.date)

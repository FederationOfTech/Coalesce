from django.forms.models import model_to_dict
from django.test import TestCase
from nose.tools import eq_, ok_

from ..serializers import TrainingDetailsSerializer
from .factories import TrainingDetailsFactory


class TestTrainingDetailsSerializer(TestCase):

    def setUp(self):
        self.opportunity_data = model_to_dict(TrainingDetailsFactory.build())

    def test_serializer_with_empty_data(self):
        serializer = TrainingDetailsSerializer(data={})
        eq_(serializer.is_valid(), False)

    def test_serializer_with_valid_data(self):
        serializer = TrainingDetailsSerializer(data=self.opportunity_data)
        ok_(serializer.is_valid())

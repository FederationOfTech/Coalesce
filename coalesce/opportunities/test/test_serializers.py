from django.forms.models import model_to_dict
from django.test import TestCase
from nose.tools import eq_, ok_

from ..serializers import CreateOpportunitySerializer
from .factories import OpportunityFactory


class TestCreateOpportunitySerializer(TestCase):

    def setUp(self):
        self.opportunity_data = model_to_dict(OpportunityFactory.build())

    def test_serializer_with_empty_data(self):
        serializer = CreateOpportunitySerializer(data={})
        eq_(serializer.is_valid(), False)

    def test_serializer_with_valid_data(self):
        serializer = CreateOpportunitySerializer(data=self.opportunity_data)
        ok_(serializer.is_valid())

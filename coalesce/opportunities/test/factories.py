import factory
import datetime


class OpportunityFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'opportunities.Opportunity'

    title = "test-opportunity"
    timestamp = datetime.datetime.fromisoformat("2020-11-26T10:50:31+00:00")
    description = "test-description"

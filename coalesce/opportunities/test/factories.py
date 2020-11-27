import factory
import datetime


class OpportunityFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'opportunities.Opportunity'

    background_check_requirements = "test-background-check-requirements"
    commitment_type = "test-commitements"
    datetime = datetime.datetime.fromisoformat("2020-11-26T10:50:31+00:00")
    description = "test-description"
    clothing_requirements = "test-clothing"
    id = 1
    location = "test-location"
    personnel_needed = 10
    post_privacy = "public"
    skills_required = ["test-skill-1", "test-skill-2"]
    title = "test-opportunity"
    # training_requirements = "test-training-requirements"

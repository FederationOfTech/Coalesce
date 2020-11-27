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
    id = factory.Faker('uuid4')
    location = "test-location"
    personnel_needed = "test-personnel"
    post_privacy = 0
    skills_required = "test-skills"
    title = "test-opportunity"
    training_requirements = "test-training-requirements"

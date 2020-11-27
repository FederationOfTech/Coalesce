import factory
from ...users.test.factories import UserFactory


class OrganizerFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'organizers.Organizer'

    user = factory.SubFactory(UserFactory)

import factory
from ...users.test.factories import UserFactory


class VolunteerFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'volunteers.Volunteer'
        django_get_or_create = ('user',)

    user = factory.SubFactory(UserFactory)
    description = 'I am a volunteer'
    skills = 'cooking, eating'
    organization = 'Camden Giving'

import factory
import datetime


class TrainingDetailsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'training_details.TrainingDetails'

    id = factory.Faker('uuid4')
    name = 'Test Training'
    link = 'https://www.federationof.tech/'
    date = datetime.date.fromisoformat('2020-11-27')

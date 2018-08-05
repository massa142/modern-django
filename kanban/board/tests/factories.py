import factory.fuzzy
from django.contrib.auth import get_user_model

from ..constants import TicketStatus
from ..models import Ticket


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()
        django_get_or_create = ('username',)

    username = factory.Faker('name')
    email = factory.Sequence(lambda n: f'person{n}@example.com')


class TicketFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ticket

    name = factory.Faker('word')
    description = factory.Faker('text')
    status = factory.fuzzy.FuzzyChoice([x.value for x in TicketStatus])
    assignee = factory.SubFactory(UserFactory)
    start = factory.Faker('date')

from django.conf import settings
from django.db import models
from model_utils.models import TimeStampedModel

from .constants import TicketStatus


class Ticket(TimeStampedModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')
    status = models.SmallIntegerField(choices=TicketStatus.get_choices(), default=TicketStatus.ToDo.value)
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL)
    start = models.DateField(null=True, blank=True)
    end = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

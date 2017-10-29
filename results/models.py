from django.contrib.postgres.fields import JSONField
from django.db import models


class Result(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    participant = models.CharField(max_length=100)
    participant_id = models.CharField(max_length=100)
    data = JSONField()

    def __unicode__(self):
        return self.participant

    class Meta:
        ordering = ('created', )

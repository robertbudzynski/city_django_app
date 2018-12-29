from django.contrib.auth.models import User as DjangoUser
from django.db import models


# Create your models here.

class User(models.Model):
    user = models.ForeignKey(DjangoUser, on_delete=None)
    places_visited = models.ManyToManyField('places.Place', blank=True, related_name='placesVisited')
    places_to_visit = models.ManyToManyField('places.Place', blank=True, related_name='placesToVisit')

    def __str__(self):
        return self.user.username

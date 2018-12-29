from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, default='')
    url_address = models.URLField(blank=True)
    image = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.title

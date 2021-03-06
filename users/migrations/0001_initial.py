# Generated by Django 2.1.4 on 2018-12-23 17:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('places', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('places_to_visit', models.ManyToManyField(blank=True, related_name='placesToVisit', to='places.Place')),
                ('places_visited', models.ManyToManyField(blank=True, related_name='placesVisited', to='places.Place')),
                ('user', models.ForeignKey(on_delete=None, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

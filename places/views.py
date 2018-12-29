from django.views import generic

from .models import Place


# Create your views here.

class ListGroups(generic.ListView):
    model = Place

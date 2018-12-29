from django.urls import path

from . import views

app_name = 'places'

urlpatterns = [
    path("", views.ListGroups.as_view(), name="all")
]

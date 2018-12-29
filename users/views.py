from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User as DjangoUser
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from places.models import Place
from .forms import AddUserForm, LoginUserForm
from .models import User


# Create your views here.

class SignUp(View):
    def get(self, request):
        form = AddUserForm()
        ctx = {'form': form}

        return render(request,
                      template_name='users/signup.html',
                      context=ctx)

    def post(self, request):
        form = AddUserForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']

            if DjangoUser.objects.filter(username=username).exists():
                return HttpResponseRedirect('/object_already_exist')

            django_user = DjangoUser.objects.create_user(username=username,
                                                         password=password,
                                                         first_name=first_name,
                                                         last_name=last_name,
                                                         email=email)
            User.objects.create(user=django_user)
            return HttpResponseRedirect(reverse('users:login'))
        return HttpResponseRedirect(reverse('users:signup'))


class LoginView(View):
    def get(self, request):
        form = LoginUserForm()
        ctx = {
            'form': form
        }
        return render(request,
                      template_name='users/login.html',
                      context=ctx)

    def post(self, request):
        form = LoginUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                """Prawidłowe logowanie"""
                login(request, user)
                return HttpResponseRedirect(reverse('users:user_details'))
            else:
                """Błędne hasło"""
                return HttpResponseRedirect(reverse('users:login'))
        else:
            """Niepoprawny formularz"""
            return HttpResponseRedirect(reverse('users:login'))


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('users:login'))


class UserDetails(View):
    def get(self, request):
        current_user = request.user
        try:
            custom_user = User.objects.get(user=current_user)
            places_visited = custom_user.places_visited.all()
            places_to_visit = custom_user.places_to_visit.all()
        except ObjectDoesNotExist:
            places_visited = None
            places_to_visit = None
        ctx = {'current_user': current_user,
               'places_visited': places_visited,
               'places_to_visit': places_to_visit}

        return render(request,
                      template_name='users/user_details.html',
                      context=ctx)


class AddVisitedView(View):
    def get(self, request, place_id):
        place = Place.objects.get(id=place_id)
        current_user = request.user
        try:
            custom_user = User.objects.get(user=current_user)
            custom_user.places_visited.add(place)
        except ObjectDoesNotExist:
            pass
        return HttpResponseRedirect(reverse('users:user_details'))


class AddToVisitView(View):
    def get(self, request, place_id):
        place = Place.objects.get(id=place_id)
        current_user = request.user
        try:
            custom_user = User.objects.get(user=current_user)
            custom_user.places_to_visit.add(place)
        except ObjectDoesNotExist:
            pass
        return HttpResponseRedirect(reverse('users:user_details'))

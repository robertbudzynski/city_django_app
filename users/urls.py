from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.LoginView.as_view(),
         name='login'),
    path('logout/', views.LogoutView.as_view(),
         name='logout'),
    path('signup/', views.SignUp.as_view(),
         name='signup'),
    path('user_details/', views.UserDetails.as_view(),
         name='user_details'),
    path('add_visited/<place_id>', views.AddVisitedView.as_view(),
         name='add_visited'),
    path('add_to_visit/<place_id>', views.AddToVisitView.as_view(),
         name='add_to_visit')
]

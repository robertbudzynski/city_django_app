from django.urls import path

from . import views

app_name = 'main_app'

urlpatterns = [
    path('history/', views.HistoryView.as_view(),
         name='history'),
    path('sport/', views.SportView.as_view(),
         name='sport'),
    path('promotion/', views.PromotionView.as_view(),
         name='promotion'),
    path('education/', views.EducationView.as_view(),
         name='education'),
    path('education/BSW', views.EducationBSW.as_view(),
         name='educationBSW'),
    path('education/UKW', views.EducationUKW.as_view(),
         name='educationUKW'),
    path('education/UMK', views.EducationUMK.as_view(),
         name='educationUMK'),
    path('education/UTP', views.EducationUTP.as_view(),
         name='educationUTP'),
    path('education/WSB', views.EducationWSB.as_view(),
         name='educationWSB'),
    path('education/WSG', views.EducationWSG.as_view(),
         name='educationWSG'),
]

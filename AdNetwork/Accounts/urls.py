from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('recovery/', views.recovery, name='recovery'),
]
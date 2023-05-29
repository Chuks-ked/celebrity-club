from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('fan-card/', views.fan_card, name='fan_card'),
    path('fan-card-application/', views.fancard_app, name='fancard_app'),
    path('meet-and-greet/', views.meet_greet, name='meet_greet'),
    path('vacation/', views.vacation, name='vacation'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('celebrity-lists/', views.celeb_list, name='celeb_list'),
]

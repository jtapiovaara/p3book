
from django.urls import path
from . import views



urlpatterns = [
    path('maili/', views.maili, name='maili'),
    path('index_mail', views.maili, name='maili'),
]
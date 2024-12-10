from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('atos_oficiais/', views.atos_oficiais, name='atos_oficiais'),
    path('ia_atos_oficiais/', views.ia_atos_oficiais, name='ia_atos_oficiais'),
]
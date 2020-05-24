from django.urls import path
from . import views


urlpatterns = [
    path('api/recom', views.recognize),
]

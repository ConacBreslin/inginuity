"""URLs for Searching the whole site"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.wholesite_search, name='wholesitesearch'),
]

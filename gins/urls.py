from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_gins, name='gins'),
    path('<int:gin_id>/', views.individual_gin, name='individual_gin'),
    path('add/', views.add_gin, name='add_gin'),
]
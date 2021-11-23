from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_distilleries, name='distilleries'),
    path('<int:distillery_id>/', views.individual_distillery, name='individual_distillery'),
    path('add/', views.add_distillery, name='add_distillery'),
]
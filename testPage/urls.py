from django.urls import path
from . import views

urlpatterns = [
    path('', views.cognitive_test, name='cognitive_test'),
]
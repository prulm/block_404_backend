from django.urls import path
from .views import *

urlpatterns = [
    path('create/', BuildingCreateView.as_view(), name='create-building'),
]
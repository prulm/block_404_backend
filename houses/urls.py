from django.urls import path
from .views import *

urlpatterns = [
    path('create/', HouseCreateView.as_view(), name='create-house'),
    path('me/', HouseListView.as_view(),  name='list-my-houses'),
]
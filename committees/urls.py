from django.urls import path
from .views import *

urlpatterns = [
    path('create/', CommitteeCreateView.as_view(), name='create-committee')
]

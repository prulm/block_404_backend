from django.urls import path
from .views import *

urlpatterns = [
    path('create/', CommitteeCreateView.as_view(), name='create-committee'),
    path('members/add/',  CommitteeMemberAddView.as_view(), name='add-committee-member'),

]

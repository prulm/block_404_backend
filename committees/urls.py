from django.urls import path
from .views import *

urlpatterns = [
    path('create/', CommitteeCreateView.as_view(), name='create-committee'),
    path('members/add/',  CommitteeMemberAddView.as_view(), name='add-committee-member'),
    path('rules/add/', CommitteeRuleAddView.as_view(), name='add-committee-rule'),
    path('reports/add/', CommitteeReportAddView.as_view(), name='add-committee-report')
]

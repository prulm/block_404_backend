from django.urls import path
from .views import *

urlpatterns = [
    path('create_payment/', PaymentCreateView.as_view(), name='create-payment'),
    path('list/<int:pk>/', PaymentListView.as_view(), name='list-buildings'),
    path('pay/', PaymentListView.as_view(), name='list-buildings'),
]
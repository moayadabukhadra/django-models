import imp
from django.urls import path
from .views import SnacksListView, SnackDetailView

urlpatterns = [
    path('snacks-list',SnacksListView.as_view(), name='snacks_list'),
    path('snack_detail/<int:pk>',SnackDetailView.as_view(), name='snack_detail'),

]
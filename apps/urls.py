from django.urls import path
from .views import EventListView, EventDetailView, EventCreateView

urlpatterns = [
    path('', EventListView.as_view(), name='event_list'),
    path('<str:id>', EventDetailView.as_view(), name='event_detail'),
    path('create/', EventCreateView.as_view(), name='event_create'),
]
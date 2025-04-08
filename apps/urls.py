from django.urls import path

from .views import EventCreateView, EventDetailView, EventListView, RegisterView, LoginView, LogoutView

urlpatterns = [
    path("", EventListView.as_view(), name="event_list"),
    path("<str:id>", EventDetailView.as_view(), name="event_detail"),
    path("create/", EventCreateView.as_view(), name="event_create"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]

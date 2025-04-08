from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView, View

from .models import Event


# Create your views here.
class EventListView(ListView):
    model = Event
    template_name = "event_list.html"
    context_object_name = "events"


class EventDetailView(DetailView):
    model = Event
    template_name = "event_detail.html"
    context_object_name = "event"
    slug_field = "id"
    slug_url_kwarg = "id"


class EventCreateView(View):
    def get(self, request):
        return render(request, "event_create.html")

    def post(self, request):
        name = request.POST.get("name")
        description = request.POST.get("description")
        date = request.POST.get("date")
        location = request.POST.get("location")
        created_by = request.user
        Event.objects.create(
            name=name,
            description=description,
            date=date,
            location=location,
            created_by=created_by,
        )

        return redirect("event_list")

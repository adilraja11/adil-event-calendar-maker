from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView, View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

from .models import Event
from .forms import UserRegistrationForm


# Create your views here.
class RegisterView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, "register.html", {"form": form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful.")
            return redirect("login")
        else:
            messages.error(request, "Registration failed. Please try again.")
            return render(request, "register.html", {"form": form})

class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, "login.html", {"form": form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("event_list")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")

        return render(request, "login.html", {"form": form})
    
class LogoutView(View):
    def post(self, request):
        logout(request)
        messages.success(request, "Logged out successfully.")
        return redirect("event_list")

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
        context = {
            'LOCATION_CHOICES': Event.LOCATION_CHOICES,
        }

        return render(request, "event_create.html", context)

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

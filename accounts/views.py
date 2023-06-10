from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render
from accounts.models import CustomUser
from django.contrib.auth.decorators import login_required

from music.util import is_spotify_authenticated
from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


@login_required
def ProfileView(request):
    user = CustomUser.objects.get(id=request.user.id)
    spotify_authenticated = is_spotify_authenticated(user)
    context = {"spotify_authenticated": spotify_authenticated}
    return render(request, "home.html", context)

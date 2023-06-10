from accounts.models import CustomUser
from django.views.generic import TemplateView
from .util import *
from django.shortcuts import render, redirect
from .credentials import REDIRECT_URI, CLIENT_SECRET, CLIENT_ID
from requests import Request, post
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    user = CustomUser.objects.get(id=request.user.id)
    spotify_authenticated = is_spotify_authenticated(user)
    context = {"spotify_authenticated": spotify_authenticated}
    return render(request, "home.html", context)


class AuthURL(TemplateView):
    def get(self, request, format=None):
        scopes = "user-read-playback-state user-modify-playback-state user-read-currently-playing"

        url = (
            Request(
                "GET",
                "https://accounts.spotify.com/authorize",
                params={
                    "scope": scopes,
                    "response_type": "code",
                    "redirect_uri": REDIRECT_URI,
                    "client_id": CLIENT_ID,
                },
            )
            .prepare()
            .url
        )
        return redirect(url)


def spotify_callback(request, format=None):
    code = request.GET.get("code")
    error = request.GET.get("error")

    response = post(
        "https://accounts.spotify.com/api/token",
        data={
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": REDIRECT_URI,
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
        },
    ).json()

    access_token = response.get("access_token")
    token_type = response.get("token_type")
    refresh_token = response.get("refresh_token")
    expires_in = response.get("expires_in")
    error = response.get("error")
    user = CustomUser.objects.get(id=request.user.id)

    update_or_create_user_tokens(
        user, access_token, token_type, expires_in, refresh_token
    )

    return redirect("/")

from django.contrib import admin
from django.urls import include, path
from accounts.views import SignUpView, ProfileView
from music import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("get-auth-url", views.AuthURL.as_view(), name="get-auth-url"),
    path("redirect", views.spotify_callback, name="redirect"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/signup/", SignUpView.as_view(), name="signup"),
    path("accounts/profile/", ProfileView, name="profile"),
]

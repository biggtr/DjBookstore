from django.urls import include, path
from .views import SignupView

urlpatterns = [
    path("signup/", SignupView, name="signup"),
    path("", include("django.contrib.auth.urls")),
]

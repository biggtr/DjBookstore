from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from allauth.account.forms import SignupForm
from django import forms
from allauth.account.models import EmailAddress


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["email", "username"]


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ["email", "username"]


class CustomSignupForm(SignupForm):
    def clean_email(self):
        email = self.cleaned_data["email"]
        if EmailAddress.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use.")
        return email

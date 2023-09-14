from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import resolve, reverse
from .forms import CustomUserCreationForm
from .views import SignupView

# Create your tests here.


class CustomUserTest(TestCase):
    def test_create_user(self):
        CustomUser = get_user_model()
        user = CustomUser.objects.create_user(
            username="bigtoto", email="torrezz2102@gmail.com", password="overpowered"
        )
        self.assertEqual(user.username, "bigtoto")
        self.assertEqual(user.email, "torrezz2102@gmail.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        CustomUser = get_user_model()
        admin_user = CustomUser.objects.create_superuser(
            username="superadmin", email="superadmin@email.com", password="testpass123"
        )
        self.assertEqual(admin_user.username, "superadmin")
        self.assertEqual(admin_user.email, "superadmin@email.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignupPageTests(TestCase):
    def setUp(self):
        url = reverse("signup")
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "registration/signup.html")
        self.assertContains(self.response, "Sign Up")
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")

    def test_signup_form(self):
        form = self.response.context.get("form")
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, "csrfmiddlewaretoken")

    def test_signup_view(self):
        view = resolve("/accounts/signup/")
        self.assertEqual(view.func.__name__, SignupView.__name__)

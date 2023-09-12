from django.test import TestCase
from django.contrib.auth import get_user_model

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

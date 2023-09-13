from django.test import SimpleTestCase, TestCase
from django.urls import resolve, reverse

from pages.views import HomepageView

# Create your tests here.


class HomePageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("home")
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template_correct(self):
        self.assertTemplateUsed(self.response, "home.html")

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, "welcome to my home page")

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "i should not be in the page")

    def test_homepage_url_resolves_homepageview(self):  # new
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomepageView.__name__)

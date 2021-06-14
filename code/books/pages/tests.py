from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView, AboutPageView
# Create your tests here.

class HomepageTests(SimpleTestCase):
    def test_home_page_status_code(self):
        resonse = self.client.get('/')
        self.assertEqual(resonse.status_code, 200)

    def test_home_page_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_homepage_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

class AboutPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def tste_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, 'about.html')

    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.response, 'About Page')

    def test_aboutpage_not_contains_incorrect_hrml(self):
        self.assertNotContains(self.response, 'Hi there! O should not be on page!')

    def test_aboutpage_url_resolve_aboutpageview(self):
        view = resolve('/about/')
        self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__)                
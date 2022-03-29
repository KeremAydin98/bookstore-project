from django.test import SimpleTestCase
from django.urls import reverse

class HomePageTests(SimpleTestCase):

    def setUp(self):

        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):

        self.assertEqual(self.response.status_code, 200)

    def test_homepage_contains_correct_html(self):

        self.assertContains(self.response, 'HomePage')

    def test_homepage_template(self):

        self.assertTemplateUsed(self.response, 'home.html')


class AboutPageTests(SimpleTestCase):

    def setUp(self):

        url = reverse('about')
        self.response = self.client.get(url)

    def test_about_page_status_code(self):

        self.assertEqual(self.response.status_code, 200)

    def test_about_page_template(self):

        self.assertTemplateUsed(self.response, 'about.html')
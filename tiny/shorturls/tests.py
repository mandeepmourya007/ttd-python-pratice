from django.test import TestCase
# from django.core.urlresolvers import reverse
from django.urls import reverse
from .models import Link


class ShortenerText(TestCase):
    def test_shortens(self):
        """
        Test that urls get shorter
        """
        url = "http://www.example.com/"
        l = Link(url=url)
        short_url = Link.shorten(l)
        self.assertLess(len(short_url), len(url))
        # self.assertTrue(len(short_url) > len(url))


    def test_recover_link(self):
        url='http://wwww.google.com'
        l=Link(url=url)
        short_url=Link.shorten(l)
        l.save()
        #to get expanded url
        exp_url = Link.expand(short_url)
        self.assertEqual(url,exp_url)
    def test_homepage(self):
        """
        Tests that a home page exists and it contains a form.
        """
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("form", response.context)
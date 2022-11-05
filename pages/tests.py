from django.test import TestCase
from django.shortcuts import reverse

from .models import Note

class UrlsLinksTest(TestCase):
    def setUp(self):
        self.note_obj = Note.objects.create(author='sina', text='sample is here.')

    def test_homepage_view_by_url_static(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_view_by_name(self):
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)
        
    def test_consciousness_view_by_url_static(self):
        response = self.client.get('/consciousness/')
        self.assertEqual(response.status_code, 200)

    def test_consciousness_view_by_name(self):
        response = self.client.get(reverse('consciousness'))
        self.assertEqual(response.status_code, 200)

    def test_manifest_consciousness_view_by_url_static(self):
        response = self.client.get('/manifest-consciousness/')
        self.assertEqual(response.status_code, 200)

    def test_manifest_consciousness_view_by_name(self):
        response = self.client.get(reverse('manifest-consciousness'))
        self.assertEqual(response.status_code, 200)

    def test_exist_author_in_page(self):
        response = self.client.get(reverse('homepage'))
        self.assertContains(response, self.note_obj.author)

    def test_exist_text_in_page(self):
        response = self.client.get(reverse('homepage'))
        self.assertContains(response, self.note_obj.text)











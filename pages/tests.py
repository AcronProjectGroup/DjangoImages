from django.test import TestCase

from django.shortcuts import reverse


class NoteListViewTest(TestCase):
    def test_homepage_view_by_url_static(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_view_by_name(self):
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)
        
    def test_consciousness_view(self):
        response = self.client.get('/consciousness/')
        self.assertEqual(response.status_code, 200)


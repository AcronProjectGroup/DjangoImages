from django.test import TestCase
from django.shortcuts import reverse

from .models import Note

class NoteListViewTest(TestCase):
    def test_notes_list_view_url(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    def test_notes_list_view_by_name(self):
        response = self.client.get(reverse("notes_list"))
        self.assertEqual(response.status_code, 200)
    def test_notes_list_page(self):
        note = Note.objects.create(author="JINA", text='Text From JINAs here.')
        response = self.client.get(reverse("notes_list"))
        self.assertContains(response, "Text From JINAs here.")
    
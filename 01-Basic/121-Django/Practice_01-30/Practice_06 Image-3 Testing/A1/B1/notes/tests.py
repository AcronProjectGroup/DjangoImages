from django.test import TestCase

class NoteListViewTest(TestCase):
    def test_notes_list_view_url(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
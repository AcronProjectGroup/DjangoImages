from django.test import TestCase
from django.urls import reverse


class HomePageTest(TestCase):
    def test_home_page_url_by_name_reversed(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    
    def test_home_page_contain_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Home')
    



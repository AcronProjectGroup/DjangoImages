from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse

from .models import Post

class BlogPostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='Sina')
        Post.objects.create(
            title  = 'Post Title',
            author = self.user,
            text =   'Some Test',
            status = Post.STATUS_CHOICES[0],
        )
    
    def test_blog_view(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_blog_view_by_name(self):
        response = self.client.get(reverse('blog'))
        self.assertEqual(response.status_code, 200)
        




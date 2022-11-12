from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse

from .models import Post

class BlogPostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='Sina')
        self.post1 = Post.objects.create(
            title  = 'Post Title',
            author = self.user,
            text =   'Some Test',
            status = Post.STATUS_CHOICES[0],
        )
    #-------------------------------------------------
    def test_blog_view(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_blog_view_by_name(self):
        response = self.client.get(reverse('blog'))
        self.assertEqual(response.status_code, 200)
    # ------------------------------------------------
    def test_find_title_on_blog(self):
        response = self.client.get(reverse('blog'))
        self.assertContains(response, 'Post Title')

    def test_find_title_on_blog_with_another_way(self):
        response = self.client.get(reverse('blog'))
        self.assertContains(response, self.post1.title)
    # ------------------------------------------------
    def test_find_title_detail_view_post(self):
        response = self.client.get('/blog/1')
        self.assertContains(response, self.post1.title)

    def test_find_text_detail_view_post(self):
            response = self.client.get('/blog/1')
            self.assertContains(response, self.post1.text)

    def test_find_title_detail_view_post_by_name(self):
            response = self.client.get(reverse('blog')+'1')
            self.assertContains(response, self.post1.title)

    def test_find_texr_detail_view_post_by_name(self):
            response = self.client.get(reverse('blog')+'1')
            self.assertContains(response, self.post1.text)

    def test_find_title_detail_view_post_by_id_Post(self):
        response = self.client.get(f'/blog/{self.post1.id}')
        self.assertContains(response, self.post1.title)

    def test_find_text_detail_view_post_by_id_Post(self):
        response = self.client.get(f'/blog/{self.post1.id}')
        self.assertContains(response, self.post1.text)



    


from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse

from .models import Post

class BlogPostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
    # def setUp(cls):
        cls.user = User.objects.create(username='Sina')
        cls.post1 = Post.objects.create(
            title  = 'Post Title',
            author = cls.user,
            text =   'Some Test',
            status = Post.STATUS_CHOICES[0][0],
        )
        cls.post2 = Post.objects.create(
            title  = '222 Post Title',
            author = cls.user,
            text =   '222 ### Some Test',
            status = Post.STATUS_CHOICES[0][0],
        )
        cls.post3 = Post.objects.create(
            title  = '3333 Post Title',
            author = cls.user,
            text =   '3333 ### Some Test',
            status = Post.STATUS_CHOICES[1][0],
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
    # ------------------------------------------------
    def test_find__status_code_detail_post_2_URL(self):
        response = self.client.get(f'/blog/{self.post2.id}')
        self.assertEqual(response.status_code, 200)
    # ------------------------------------------------
    def test_find_status_code_detail_post_1_by_name(self):
        response = self.client.get(reverse('blog_detail_view', args=[self.post1.id]))
        self.assertEqual(response.status_code, 200)
    # ------------------------------------------------
    def test_find_status_code_404_if_post_id_not_exist(self):
        response = self.client.get('/blog/'+ '123123asd')
        self.assertEqual(response.status_code, 404)
    # ------------------------------------------------
    def test_draft_post_dont_show_in_blog(self): # TDD   Test Driven Development 
        response= self.client.get(reverse('blog'))
        self.assertContains(response, self.post1.title)        
        self.assertNotContains(response, self.post3.title)        



    


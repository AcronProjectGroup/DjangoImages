from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse

from .models import Post

class BlogPostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="user1")
        self.post1 = Post.objects.create(
            title="Post1",
            text="This is the description of Post1",
            status=Post.STATUS_CHOICES[0],
            author=self.user,
        )
    # My first testing is Greeen :)
    # 1
    def testIDExistInBlog(self):
        response = self.client.get("/blog/")
        self.assertContains(response, self.post1.id)
    # Another:
    # 2
    def test_post_list_url(self):
        response = self.client.get("/blog/")
        self.assertEqual(response.status_code, 200)
    # 3
    def test_post_list_url_by_name(self):
        response = self.client.get(reverse("posts_list"))
        self.assertEqual(response.status_code, 200)
    # 4
    def test_post_title_on_blog_list_page(self):
        response = self.client.get(reverse("posts_list"))
        self.assertContains(response, self.post1.title)
    # 5
    def test_post_details_on_blog_detail_page(self):
        response = self.client.get('/blog/1/')
        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post1.text)
    # 6
    def test_post_detail_url_by_name(self):
        response = self.client.get(reverse('post_detail', args=[self.post1.id]))
        self.assertEqual(response.status_code, 200)
    # 7
    def testByFString(self):
        response = self.client.get(f'/blog/{self.post1.id}/')
        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post1.text)
    # 8
    def test_status_404_if_post_id_not_exist(self):
        response = self.client.get(reverse('post_detail', args=[(self.post1.id)+1]))
        self.assertEqual(response.status_code, 404)

    

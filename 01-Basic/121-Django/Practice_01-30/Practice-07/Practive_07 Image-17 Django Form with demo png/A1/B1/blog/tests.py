from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse

from .models import Post

class BlogPostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username="user1")
        cls.post1 = Post.objects.create(
            title="Post1",
            text="This is the description of Post1",
            status=Post.STATUS_CHOICES[0][0], # Published
            author=cls.user,
        )
        cls.post2 = Post.objects.create(
            title="Post2",
            text="Lorem",
            status=Post.STATUS_CHOICES[1][0], # Draft
            author=cls.user,
        )

    # def setUp(self):
    #     self.user = User.objects.create(username="user1")
    #     self.post1 = Post.objects.create(
    #         title="Post1",
    #         text="This is the description of Post1",
    #         status=Post.STATUS_CHOICES[0][0], # Published
    #         author=self.user,
    #     )
    #     self.post2 = Post.objects.create(
    #         title="Post2",
    #         text="Lorem",
    #         status=Post.STATUS_CHOICES[1][0], # Draft
    #         author=self.user,
    #     )
    # My first testing is Greeen :)
    # 1
    def testIDExistInBlog(self):
        response = self.client.get("/blog/")
        self.assertContains(response, self.post1.id)
    # These are The Unit Test
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
        response = self.client.get(reverse('post_detail', args=[(self.post1.id)+3]))
        self.assertEqual(response.status_code, 404)
    # 9 TDD -> Test Driver Development
    def test_draft_post_not_show_in_posts_list(self):
        response = self.client.get(reverse("posts_list"))
        self.assertContains(response, self.post1.title)
        self.assertNotContains(response, self.post2.title)

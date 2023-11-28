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
    # 10
    def test_post_model_str(self):
        post = self.post1
        str_model = str(self.user)+":"+post.title
        self.assertEqual(str(post), str_model)
    # 11
    def test_post_detail(self):
        self.assertEqual(self.post1.title, "Post1")
        self.assertEqual(self.post1.text, "This is the description of Post1")
    # 12
    def test_post_create_view(self):
        response = self.client.post(reverse("post_create"), {
            "title": "Some Title",
            "text": "Some Text",
            "status": "pub",
            "author": self.user.id,
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Post.objects.last().title, "Some Title")
        self.assertEqual(Post.objects.last().text, "Some Text")
    # 13
    def test_post_update_view(self):
        response = self.client.post(reverse("post_update", args=[self.post2.id]),{
            "title": "PostUpdated",
            "text":  "textUpdated",
            "status": "pub",
            "author": self.post2.author.id,
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Post.objects.last().title, "PostUpdated")
        self.assertEqual(Post.objects.last().text,  "textUpdated")
    # 14
    def test_post_delete_view(self):
        response = self.client.post(reverse("post_delete", args=[self.post1.id]))
        self.assertEqual(response.status_code, 302)







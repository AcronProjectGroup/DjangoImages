from django.db import models
from django.shortcuts import reverse

class Post(models.Model):
    # Status Should be just two case
    STATUS_CHOICES = (
        ("pub", "Published"),
        ("drf", "Drafts"),
    )
    # title
    title = models.CharField(max_length=100)
    # text
    text = models.TextField()
    # author
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    # date
    date_created = models.DateTimeField(auto_now_add=True)
    # date modified
    datatime_modified = models.DateTimeField(auto_now=True)
    # status
    status = models.CharField(choices=STATUS_CHOICES, max_length=3)

    def __str__(self):
        return f"{self.author}:{self.title}"

    def get_absolute_url(self):
        return reverse("post_detail", args=[self.id]) # for example : blog/1 OR blog/23
    
    
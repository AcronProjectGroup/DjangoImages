from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Post(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    cover = models.ImageField(upload_to='covers/', blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("book_detail", args=[self.id])





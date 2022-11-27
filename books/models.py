from django.db import models
from django.urls import reverse

class Book(models.Model):
    title = models.CharField(max_length=200)
    bokk_author = models.CharField(max_length=200)
    book_description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    

    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse("book_detail_view", args=[self.id])
    

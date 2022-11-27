from django.db import models


class BookModel(models.Model):
    title = models.CharField(max_length=200)
    bokk_author = models.CharField(max_length=200)
    book_description = models.TextField()
    price = models.IntegerField(max_length=8)
    

    def __str__(self):
        return self.title
    


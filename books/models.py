from django.db import models


class BookModel(models.Model):
    title = models.CharField(max_length=200)
    bokk_author = models.CharField(max_length=200)
    book_description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)


    def __str__(self):
        return self.title
    


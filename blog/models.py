from django.db import models


class Post(models.Model):

    STATUS_CHOICES = (
        ('pub', 'Published'),
        ('drf', 'Draft'),
    )
    # photo = models.ImageField()
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date_time_created = models.DateTimeField(auto_now_add=True)
    date_time_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=3)

    def __str__(self):
        return self.title
    

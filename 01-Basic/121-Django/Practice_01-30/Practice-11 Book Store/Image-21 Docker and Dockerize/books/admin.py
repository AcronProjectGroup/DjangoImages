from django.contrib import admin

from .models import Book
from .models import Comment


@admin.register(Comment)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'text', 'datetime_created', 'recommend', 'is_active', )




@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'author',  )
# admin.site.register(Comment, CommentAdmin)






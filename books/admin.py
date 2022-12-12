from django.contrib import admin

from .models import Book, Comment


class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Book)
admin.site.register(Comment)




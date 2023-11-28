from django.contrib import admin

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "title", "status", "date_created")
    ordering = ("date_created",)

# admin.site.register(Post, PostAdmin)

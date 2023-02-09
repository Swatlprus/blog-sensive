from django.contrib import admin
from blog.models import Post, Tag, Comment

class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ('author', 'likes', 'tags', )

class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'published_at')
    raw_id_fields = ('author', 'post', )

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)

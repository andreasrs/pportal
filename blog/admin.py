from django.contrib import admin
from blog.models import Post, Comment, Message

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Message)


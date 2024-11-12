from django.contrib import admin

from .models import User, UserFollow, Post, PostLike, PostComment

# Register your models here.
admin.site.register(User)
admin.site.register(Post)
admin.site.register(UserFollow)
admin.site.register(PostComment)
admin.site.register(PostLike)

from django.contrib.auth.models import AbstractUser
from django.db import models
from app.manager import UserManager


# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=130, unique=True)
    bio = models.CharField(max_length=164, blank=True, null=True)
    password = models.CharField(max_length=120)
    phone = models.CharField(max_length=12,blank=True, null=True)
    city = models.CharField(max_length=80, blank=True, null=True)



    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField( default=False)
    is_superuser = models.BooleanField( default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()


class Post(models.Model):
    title = models.CharField(max_length=130)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='liked_posts')


class PostLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('user', 'post'),)


class PostComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


class UserFollow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
    follows = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followers")

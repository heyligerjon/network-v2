from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Follower:
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    following = models.ManyToManyField(User)

class Post:
    postedBy = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField()
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    friends = models.ManyToManyField("self")

class Status(models.Model):
    statusId = models.UUIDField()
    postedBy = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField()

class Comment(models.Model):
    commentBy = models.ForeignKey(User, on_delete=models.CASCADE)
    commentPost = models.ForeignKey(Status, on_delete=models.CASCADE)
    content = models.CharField()

class Reaction(models.Model):
    reactBy = models.ForeignKey(User, on_delete=models.CASCADE)
    reactPost = models.ForeignKey(Status, on_delete=models.CASCADE)
    reaction = models.CharField()

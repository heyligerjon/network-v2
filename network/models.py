from django.contrib.auth.models import AbstractUser
from django.db import models
from emoji import get_emoji_unicode_dict

class User(AbstractUser):
    friends = models.ManyToManyField("self")

class Status(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="statuses")
    body = models.CharField(max_length=560)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"${self.postedBy}'s Status: {self.body}"

    def serialize(self):
        return {
            "id": self.id,
            "body": self.body,
            "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p")
        }

class Comment(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="comments_made")
    commentPost = models.ForeignKey("Status", on_delete=models.CASCADE, related_name="comments")
    body = models.CharField(max_length=560)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"${self.commentBy}: {self.body}"
        
    def serialize(self):
        return {
            "id": self.id,
            "commentPost": self.commentPost,
            "body": self.body,
            "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p")
        }

class Reaction(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="reactions_sent")
    reactPost = models.ForeignKey("Status", on_delete=models.CASCADE, related_name="reactions")
    reaction = models.CharField(max_length=2)

    def __str__(self):
        return self.reaction

    def is_emoji(self):
        count = 0
        for emoji in get_emoji_unicode_dict:
            count += self.count(emoji)
            if count > 1:
                return False
        return bool(count)

    def serialize(self):
        return {
            "id": self.id,
            "reactPost": self.reactPost,
            "reaction": self.reaction
        }
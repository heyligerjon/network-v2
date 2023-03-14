from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from .models import *
from .serializers import *

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    lookup_field = "username"
    queryset = User.objects.all()

class StatusViewSet(viewsets.ModelViewSet):
    serializer_class = StatusSerializer
    def get_queryset(self):
        user = User.objects.get(username=self.kwargs['user_username'])
        return Status.objects.filter(user=user)

    def list_friends(self, request, user_pk=None):
        user = User.objects.get(pk=user_pk)
        return Status.objects.filter(user__in=user.friends)

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    def get_queryset(self):
        user = User.objects.get(username=self.kwargs['user_username'])
        commentPost = Status.objects.get(pk=self.kwargs['user_status_pk']) 
        return Comment.objects.filter(user=user, commentPost=commentPost)

class ReactionViewSet(viewsets.ModelViewSet):
    serializer_class = ReactionSerializer
    def get_queryset(self):
        user = User.objects.get(username=self.kwargs['user_username'])
        reactPost = Status.objects.get(pk=self.kwargs['user_status_pk']) 
        return Reaction.objects.filter(user=user, reactPost=reactPost)
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from .models import *
from .serializers import *

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    lookup_field = "username"
    queryset = User.objects.all()

# Status will neet to be converted to reg ViewSet to list user statuses
class StatusViewSet(viewsets.ModelViewSet):
    serializer_class = StatusSerializer
    def get_queryset(self):
        user = User.objects.get(username=self.kwargs['user_username'])
        return Status.objects.filter(user=user)
    
    # def create(self):
    #     pass

    # def retrieve(self):
    #     pass

    # def update(self):
    #     pass

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
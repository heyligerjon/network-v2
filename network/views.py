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
        return Status.objects.filter(pk=self.kwargs['user_username'])

# class CommentViewSet(viewsets.ModelViewSet):
#     serializer_class = CommentSerializer
#     post = StatusViewSet.retrieve()
#     queryset = Comment.objects.all(commentPost=post)
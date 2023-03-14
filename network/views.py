import json
import emoji
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions
from rest_framework.response import Response

from .models import *
from .serializers import *

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    lookup_field = "username"
    queryset = User.objects.all()

class StatusViewSet(viewsets.ModelViewSet):
    serializer_class = StatusSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        user = User.objects.get(username=self.kwargs['user_username'])
        return Status.objects.filter(user=user)

    def list_friends(self, request, user_pk=None):
        user = User.objects.get(pk=user_pk)
        return Status.objects.filter(user__in=user.friends)

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        user = User.objects.get(username=self.kwargs['user_username'])
        commentPost = Status.objects.get(pk=self.kwargs['user_status_pk']) 
        return Comment.objects.filter(user=user, commentPost=commentPost)

class ReactionViewSet(viewsets.ModelViewSet):
    serializer_class = ReactionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        user = User.objects.get(username=self.kwargs['user_username'])
        reactPost = Status.objects.get(pk=self.kwargs['user_status_pk']) 
        return Reaction.objects.filter(user=user, reactPost=reactPost)
    
# def get_friends(request):
#     friends = [request.user]

#     try:
#         friendsObj = request.user.friends.all()
#     except:
#         friendsObj = None
    
#     for friend in friendsObj:
#         if friend not in friends:
#             friends.append(friend)

#     return friends

# def get_statuses(user_list):

#     try:
#         statuses = Status.objects.filter(user__in=user_list)
#         statuses.order_by("-timestamp").all()
#     except:
#         statuses = None

#     return statuses

# def home(request):
#     if request.user.is_authenticated:

#         # Retrieve the user's friends to determine statuses to show
#         friends = get_friends(request)

#         # TODO
#         # For now, get all statuses. When friend functionality is added, constrain
#         statuses = get_statuses(User.objects.all())

#         if statuses:    
#             return JsonResponse(
#                 [status.serialize() for status in statuses], 
#                 safe=False
#             )
#     else:
#         return HttpResponseRedirect(reverse("login"))

# def login_view(request):
#     if request.method == "POST":

#         # Attempt to sign user in
#         username = request.POST["username"]
#         password = request.POST["password"]
#         user = authenticate(request, username=username, password=password)

#         # Check if authentication successful
#         if user is not None:
#             login(request, user)
#             return HttpResponseRedirect(reverse("index"))
#         else:
#             return render(request, "network/login.html", {
#                 "message": "Invalid username and/or password."
#             })
#     else:
#         return render(request, "network/login.html")

# def logout_view(request):
#     logout(request)
#     return HttpResponseRedirect(reverse("index"))

# def register(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         email = request.POST["email"]

#         # Ensure password matches confirmation
#         password = request.POST["password"]
#         confirmation = request.POST["confirmation"]
#         if password != confirmation:
#             return render(request, "network/register.html", {
#                 "message": "Passwords must match."
#             })

#         # Attempt to create new user
#         try:
#             user = User.objects.create_user(username, email, password)
#             user.save()
#         except IntegrityError:
#             return render(request, "network/register.html", {
#                 "message": "Username already taken."
#             })
#         login(request, user)
#         return HttpResponseRedirect(reverse("index"))
#     else:
#         return render(request, "network/register.html")

# @csrf_exempt
# def status_view(request, statusId):

#     #Retrieve status from id, retrieve comments from statusId and display all
#     status = Status.objects.get(id=statusId, user=request.user)
#     comments = Comment.objects.filter(commentPost=status)
#     numReactions = Reaction.objects.filter(reactPost=status).count()
    
#     # Eventually will want to expand reactions object for full emoji support and 
#     # filter for more data

#     return render(request, "network/status.html", {
#         "status": status,
#         "comments": comments,
#         "reactions": numReactions
#     })

# @csrf_exempt
# @login_required
# def status_new(request):
#     # New status must be created via POST
#     if request.method != "POST":
#         return JsonResponse({"error": "POST request required"}, status=400)
    
#     data = json.loads(request.body)

#     postedBy = request.user
#     content = data.get("body", "")

#     status = Status(
#         user=postedBy,
#         body=content
#     )
#     status.save()
#     # Display form to add new status
#     return JsonResponse({"message": "Status updated successfully."}, status=201)

# @login_required
# def status_edit(request, statusId):
#     # Retrieve status if statusId, blank new form if null
#     try:
#         status = Status.objects.get(id=statusId, user=request.user)
#     except Status.DoesNotExist:
#         error = '404 Error: Status not found'

#     if request.method != "PUT":
#         return JsonResponse({"error": "PUT request required"}, status=404)

#     data = json.loads(request.body)

#     if data.get("body", "") is not None:
#         status.body = data["body"]
#     status.save()

#     return JsonResponse({"message": "Status updated successfully."}, status=200)

# def profile_view(request, username):
#     # Retrieve user details, friends, and status history to display on profile
#     user = User.objects.get(username=username)
#     statuses = get_statuses(User.objects.filter(username=username))
#     numFriends = user.friends.all().count()

#     return render(request, "network/profile.html",{
#         "user": user,
#         "statuses": statuses,
#         "friends": numFriends
#     })

# def profile_edit(request, username):

#     # Validate request and retrieve data
#     if request.method != "POST":
#         return JsonResponse({"error": "POST request required"}, status=400)
    
#     data = json.loads(request.body)

#     # Retrieve user and update with request info
#     try:
#         user = User.objects.get(username=username)
#     except User.DoesNotExist:
#         return JsonResponse({
#             "error": f"User '{username}' does not exist."
#         })
#     user.username = data.get("username")
#     user.first_name = data.get("firstName")
#     user.last_name = data.get("lastName")
#     user.email = data.get("email")
#     user.save()
    
#     return JsonResponse({"message": "Profile updated successfully."}, status=200)

# def friends_list(request, username):

#     # Retrieve all friends by username
#     user = User.objects.get(username=username)
#     friends = user.friends.all()

#     # Retrieve most recent status from friend to display

#     context = {
#         "data": serializers.serialize('json', friends, fields=('id', 'username', 'first_name', 'last_name'))
#     }
#     return JsonResponse(context)

# @csrf_exempt
# @login_required
# def comment(request, statusId):
    
#     if request.method != "POST":
#         return JsonResponse({"error": "POST request required"}, status=400)
#     data = json.loads(request.body)

#     # Convert username to user object
#     username = data.get("username", "")
#     try:
#         user = User.objects.get(username=username)
#     except User.DoesNotExist:
#         return JsonResponse({
#             "error": f"User '{username}' does not exist."
#         })
    
#     # Get necessary data and create comment object
#     body = data.get("body", "")
#     try:
#         status = Status.objects.get(id=statusId)
#     except Status.DoesNotExist:
#         return JsonResponse({
#             "error": f"Status id:{statusId} does not exist for '{username}'"
#         })
#     comment = Comment(
#         user=user,
#         commentPost=status,
#         body=body
#     )
#     comment.save()
#     return JsonResponse({
#         "message": "Comment added successfully",
#         "commentId": comment.id
#         })

# def react(request, statusId):
#     if request.method != "POST":
#         return JsonResponse({"error": "POST request required"}, status=400)
    
#     post = Status.objects.get(id=statusId)

#     reaction = Reaction(
#         user=request.user,
#         reactPost=post,
#         reaction=emoji.emojize(':thumbsup:')
#     )
#     reaction.save()

#     # In future will filter by react type and display counts for each
#     numReacts = Reaction.objects.filter(reactPost=post).count()

#     return JsonResponse({
#         "message": "Liked",
#         "reactId": reaction.id,
#         "reactions": numReacts
#     }, status=200)
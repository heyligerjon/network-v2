import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import User, Status, Comment, Reaction

def index(request):

    # Authenticated users view their inbox
    if request.user.is_authenticated:
        return render(request, "network/home.html")

    # Everyone else is prompted to sign in
    else:
        return HttpResponseRedirect(reverse("login"))

def get_friends(request):
    friends = [request.user]

    try:
        friendsObj = request.user.friends.all()
    except:
        friendsObj = None
    
    for friend in friendsObj:
        if friend not in friends:
            friends.append(friend)

    return friends

def home(request):
    if request.user.is_authenticated:

        # Retrieve the user's friends to determine statuses to show
        friends = get_friends(request)

        try:
            statuses = Status.objects.filter(user__in=friends)
        except:
            statuses = None

        statuses.order_by("-timestamp").all()
        if statuses:    
            return JsonResponse(
                [status.serialize() for status in statuses], 
                safe=False
            )
    else:
        return HttpResponseRedirect(reverse("login"))

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

def status_view(request, statusId):
    #Retrieve status from id, retrieve comments from statusId and display all
    return render(request, "network/status.html")

@csrf_exempt
@login_required
def status_new(request):
    # New status must be created via POST
    if request.method != "POST":
        return JsonResponse({"error": "POST request required"}, status=400)
    
    data = json.loads(request.body)

    postedBy = request.user
    content = data.get("body", "")

    status = Status(
        user=postedBy,
        body=content
    )
    status.save()
    # Display form to add new status
    return JsonResponse({"message": "Status updated successfully."}, status=201)

def status_edit(request, statusId):
    # Retrieve status if statusId, blank new form if null
    # Display prefilled form for update
    return JsonResponse({"message": "Status updated successfully."}, status=201)

def profile_view(request, username):
    # Retrieve all profile details
    # Retrieve status history
    return render(request, "network/profile.html")

def profile_edit(request, username):
    # Retrieve all profile details
    # Display prefilled form for changes
    return render(request, "network/profile.html")

def friends_list(request, username):
    # Retrieve all friends by username
    return render(request, "network/friends.html")

def comment(request):
    pass
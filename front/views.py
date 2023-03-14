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
from django.core import serializers

# from .models import User, Status, Comment, Reaction

def index(request, route=None):
    path = None

    if route == 'login':
        path = 'login'
    elif route == 'register':
        path = 'register'
    
    return render(request, "frontend/layout.html",{
        path: route 
    })
    # # Authenticated users view their inbox
    # if request.user.is_authenticated:
    #     return render(request, "network/home.html")

    # # Everyone else is prompted to sign in
    # else:
    #     return HttpResponseRedirect(reverse("login"))
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

from .models import Profile
# Create your views here.


def index(request):
    return render(request, "testmodule/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username,
                            password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            
            # if identification in student and can be verified
            # go to student
            # if identification in student and can be verified
            # go to student
             
            return HttpResponse("login successfully")
        else:
            return render(request, "testmodule/studentmain.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "testmodule/index.html")

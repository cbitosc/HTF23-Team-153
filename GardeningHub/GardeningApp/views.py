from django.shortcuts import render, redirect
from django.urls import path
from .forms import *
from django.http import HttpResponse
from .helpers import verify, checkUsernameDuplication

# Create your views here.


def takeMeHome(requst):
    return redirect("home/")


def homePage(request, username):
    context = {"new_user_details": username}
    return render(request, "Entry/home.html", context)


def login(request):
    login_input = LoginForm()
    if request.method == "POST":
        login_input = LoginForm(request.POST)
        username = login_input["userName"].value()
        password = login_input["password"].value()
        if verify(username, password):
            # welcomeContext = {"new_user_details": request.POST.dict()["userName"]}
            return redirect(f"/GardeningApp/home/{username}")
            # return render(request, "Entry/home.html", welcomeContext)
        else:
            context = {"login_details": login_input, "issue": "wrongPassword"}
            return render(request, "Entry/login.html", context)
    elif request.method == "GET":
        context = {"login_details": login_input}
        return render(request, "Entry/login.html", context)
    return HttpResponse("Shit aint happen")


# 2) signUp page -> starts signup form process
def signUp(request):
    # create blank form
    details_of_SignUpForm = SignUpForm()
    context = {"new_user_details": details_of_SignUpForm}

    # if metho is POST and data is valid->
    # then new user is saved and directed to home/
    if request.method == "POST":
        details_of_SignUpForm = SignUpForm(request.POST)
        if checkUsernameDuplication(request.POST.dict()["userName"]):
            context = {
                "new_user_details": details_of_SignUpForm,
                "issue": "UsernameDuplication",
            }
            return render(request, "Entry/signUp.html", context)
        if details_of_SignUpForm.is_valid():
            details_of_SignUpForm.save()
            context = {"new_user_details": details_of_SignUpForm}
            welcomContext = {"new_user_details": request.POST.dict()["userName"]}
            return render(request, "Entry/home.html", welcomContext)

    # if new user has to be registered, blank form will be rendered
    elif request.method == "GET":
        return render(request, "Entry/signUp.html", context)
    return HttpResponse("Invalid Request")

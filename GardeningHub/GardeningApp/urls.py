from django.urls import path
from GardeningApp import views

urlpatterns = [
    # 1) starting from sign up page
    path("", views.takeMeHome, name="default"),
    # path("home/",views.homePage)
    path("home/<str:username>/", views.homePage, name="homePage"),
    path("signup/", views.signUp, name="signUpPage"),
    path("login/", views.login, name="loginPage"),
    # path("myaccount/", views, name="accountPage"),
]

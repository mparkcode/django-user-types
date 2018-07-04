from django.urls import path
from .views import login, register_buyer, register_seller, logout, profile

urlpatterns = [
    path('login', login, name="login"),
    path('logout', logout, name="logout"),
    path('profile', profile, name="profile"),
    path('register/buyer', register_buyer, name="register_buyer"),
    path('register/seller', register_seller, name="register_seller"),
]

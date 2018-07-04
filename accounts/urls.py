from django.urls import path
from .views import login, register, logout, profile

urlpatterns = [
    path('login', login, name="login"),
    path('logout', logout, name="logout"),
    path('profile', profile, name="profile"),
    path('register', register, name="register"),
]

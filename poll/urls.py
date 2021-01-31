from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="home"),
    path('contestant', views.contestant, name="contestant"),
    path('profile', views.profile, name="profile"),
    path('vote', views.vote, name="vote"),
    path('vote_now/<int:id>', views.vote_now, name="vote_now"),
    path('profile_view/<int:id>', views.profile_view, name="profile_view"),
    path('signup', views.signup, name="signup"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('result', views.result, name="result"),
]


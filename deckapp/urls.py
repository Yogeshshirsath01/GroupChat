from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path("",views.index, name="index"),
    path("groups/<str:pk>",views.group_chat, name="group_chat"),
    path("create",views.create, name="create"),
    path("signup",views.signup, name="signup"),
    path("login",views.login_view, name="login"),
    path("logout",views.logout_view, name="logout"),
    path("postedit",views.postedit, name="postedit"),
    path("send",views.send, name="send"),
    path("deckauth/<str:pk>",views.deckauth, name="deckauth"),
    path('getMessages/<str:pk>', views.getMessages, name='getMessages'),
] 

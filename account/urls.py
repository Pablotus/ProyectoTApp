from account import views
from django.urls import path
from django.urls import path, include
from account.views import *
from django.contrib.auth.views import LogoutView




urlpatterns = [
    path('login/', login_account, name="login"),
    path('logout/', LogoutView.as_view(template_name="account/logout.html"), name="logout"),
    #path('logout/', views.logout, name="logout"),
    #path('login/', views.login, name="login"),
]
from django.urls import path
from .import views

urlpatterns = [
    path('', views.books),
    path('login',views.login, name="login"),
    path('signup',views.signup, name='signup'),
    path('slogin',views.slogin, name='slogin'),
    path('ssignup',views.ssignup, name='ssignup')
]
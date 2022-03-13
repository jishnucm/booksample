from django.urls import path
from .import views

urlpatterns = [
    path('', views.books),
    path('login1',views.login)
]
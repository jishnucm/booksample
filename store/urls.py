from django.urls import path
from .import views

urlpatterns = [
    path('/', views.books),
    path('login',views.login, name="login")
]
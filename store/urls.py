from django.urls import path
from .import views

urlpatterns = [
    path('/', views.books),
    path('/',views.login,name="login")
]
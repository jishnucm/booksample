from django.urls import path
from .import views

urlpatterns = [
    path('admin2/', views.books)
]
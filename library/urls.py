from django.urls import path
from . import views

urlpatterns = [
    path('', views.books_list, name='books_list'),
    path('search/', views.search_books, name='search_books'),
]

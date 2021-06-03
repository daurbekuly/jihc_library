from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeBooks.as_view(), name='home'),
    path("search/", Search.as_view(), name="search"),
    path('ebook/<slug:slug>/', BookDetailView.as_view(), name='ebook_page'),
    path('add_books/', AddBook.as_view(), name='add_books'),
    path('genres/<slug:slug>/', BooksByGenre.as_view(), name='genres'),
    path('genre_list/genres/', GenreList.as_view(), name='genre_list'),
    path('author_list/authors/', AuthorList.as_view(), name='author_list'),
    path('authors/<str:slug>/', AuthorDetailView.as_view(), name='author_page'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),

]

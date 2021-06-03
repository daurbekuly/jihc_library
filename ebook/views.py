from django.contrib import messages
from django.contrib.auth import login, logout
from django.db.models import Q
from django.shortcuts import render, redirect
from .forms import BookForm, UserRegisterForm, UserLoginForm
from .models import *
from django.views.generic import ListView, DetailView, CreateView


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации!')
    else:
        form = UserRegisterForm()
    return render(request, 'ebook/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'ebook/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


class HomeBooks(ListView):
    model = Book
    template_name = 'ebook/home_books.html'
    context_object_name = 'book'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    genre = Genre.objects.all()[:7]
    extra_context = {'genre': genre}

    queryset = Book.objects.filter(draft=False).prefetch_related('authors')


class BooksByGenre(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'ebook/books_by_genre.html'
    allow_empty = False
    paginate_by = 10
    slug_field = "url"

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # context['genre'] = Genre.objects.get(url=self.kwargs['slug'])
    #     return context

    def get_queryset(self):
        genre_name = self.kwargs['slug']
        genre = Genre.objects.get(url=genre_name)
        return Book.objects.filter(genres=genre, draft=False).select_related('category').prefetch_related('authors')


class AddBook(CreateView):
    form_class = BookForm
    template_name = 'ebook/add_books.html'


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book_item'
    template_name = 'ebook/ebook_page.html'

    books = Book.objects.all()
    extra_context = {'books': books}

    slug_field = "url"


class GenreList(ListView):
    model = Genre
    template_name = 'ebook/genre_list.html'
    context_object_name = 'genre'


class AuthorList(ListView):
    model = Author
    template_name = 'ebook/author_list.html'
    context_object_name = 'authors'


class AuthorDetailView(DetailView):
    model = Author
    context_object_name = 'author'
    template_name = 'ebook/author_page.html'

    slug_field = 'name'


class Search(ListView):
    paginate_by = 10
    context_object_name = 'book'
    template_name = 'ebook/home_books.html'

    def get_queryset(self):  # новый
        return Book.objects.filter(title__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context

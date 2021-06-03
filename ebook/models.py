from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Author(models.Model):
    name = models.CharField("Имя", max_length=100)
    birthdate = models.PositiveSmallIntegerField("Год рождения", default=0)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="authors/")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('author_page', kwargs={"slug": self.name})

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Genre(models.Model):
    name = models.CharField("Имя", max_length=100)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("genre", kwargs={"slug": self.url})

    def get_absolute_url(self):
        return reverse('genres', kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Book(models.Model):
    title = models.CharField("Название", max_length=100)
    tagline = models.CharField("Слоган", max_length=100, default='', blank=True, null=True)
    description = models.TextField("Описание")
    poster = models.ImageField("Постер", upload_to="books/")
    year = models.PositiveSmallIntegerField("Дата выхода", default=2000)
    authors = models.ManyToManyField(Author, verbose_name="авторы", related_name="book_author")
    genres = models.ManyToManyField(Genre, verbose_name="жанры")
    category = models.ForeignKey(Category, verbose_name="категория", on_delete=models.SET_NULL, null=True)
    epub = models.FileField(upload_to='documents/epub/', blank=True, null=True)
    pdf = models.FileField(upload_to='documents/pdf/', null=True)
    mobi = models.FileField(upload_to='documents/mobi/', blank=True, null=True)
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("ebook_page", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Электронная Книга"
        verbose_name_plural = "Электронные Книги"

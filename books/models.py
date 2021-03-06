from django.db import models


# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField(blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Author(models.Model):
    salutation = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    books = models.ManyToManyField('Book')
    internet = models.URLField(blank=True)
    headshot = models.ImageField(upload_to='author_headshots')

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    book_image = models.ImageField(blank=True)
    pages = models.CharField(blank=True, max_length=8)
    kirjailija = models.CharField(blank=True, max_length=200)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title

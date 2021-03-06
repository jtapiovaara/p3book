from django.shortcuts import render
from django.views.generic import ListView, DetailView

from books.models import Publisher, Book, Author


class BookList(ListView):
    model = Book
    context_object_name = 'books_by_tapsa'


class BookDetail(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    pass

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Book.objects.filter()


class AuthorList(ListView):
    model = Author
    context_object_name = 'authors_with_tapsa_twix'


def authordetail(request, pk):
    author_yx = Author.objects.get(pk=pk)
    authors_books = Book.objects.filter(author__id=author_yx.id)

    context = {
        'author_yx': author_yx,
        'authors_books': authors_books
    }
    return render(request, 'books/author_detail.html', context)


class PublisherList(ListView):
    model = Publisher
    context_object_name = 'my_favorite_publishers'


def publisherdetail(request, pk):

    publisher_yx = Publisher.objects.get(pk=pk)
    publishers_books = Book.objects.filter(publisher_id=pk)

    context = {
        'publisher_yx': publisher_yx,
        'publishers_books': publishers_books
    }
    return render(request, 'books/publisher_detail.html', context)









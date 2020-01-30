from django.urls import path, include
from . import views

app_name = 'books'

urlpatterns = [
    path('books/', views.BookList.as_view(), name='books'),
    path('authors/', views.AuthorList.as_view(), name='authors'),
    path('publishers/', views.PublisherList.as_view(), name='publishers'),
    # path('book/<publisher>', views.ListView.as_view(), name='booksbypublisher'),
    # path('author/<int:pk>', views.ListView.as_view(), name='authorsbooks'),
    path('book/<int:pk>', views.BookDetail.as_view(), name='bookdetail'),
    path('authors/<int:pk>', views.AuthorDetail, name='authordetail'),
    path('publishers/<int:pk>', views.publisherdetail, name='publisherdetail'),
]
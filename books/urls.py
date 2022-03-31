from .views import BookListView, BookDetailView
from django.urls import path

urlpatterns = [
    path('',BookListView.as_view(), name='book_list'),
    path('<uuid:pk>/', BookDetailView.as_view(), name='book_detail')
]
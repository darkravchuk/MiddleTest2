from django.shortcuts import render
from .models import Book, Author
from django.db.models import Count


def books_view(request):
    # Отримуємо 5 останніх доданих до бази даних книг
    latest_books = Book.objects.order_by('-publication_date')[:5]

    # Передаємо список останніх книг у шаблон та відображаємо його
    return render(request, 'books.html', {'books': latest_books})



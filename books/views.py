from django.shortcuts import render
from .models import Book, Author
from django.db.models import Count


def books_view(request):
    # Отримуємо 5 останніх доданих до бази даних книг
    latest_books = Book.objects.order_by('-publication_date')[:5]

    # Передаємо список останніх книг у шаблон та відображаємо його
    return render(request, 'book_list.html', {'books': latest_books})


def authors_view(request):
    # Отримати всіх авторів та кількість книг, які вони написали
    authors_with_books_count = Author.objects.annotate(num_books=Count('book'))

    # Передати список авторів разом з кількістю книг у шаблон та відобразити його
    return render(request, 'author_list.html', {'authors': authors_with_books_count})
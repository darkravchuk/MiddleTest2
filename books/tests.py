from django.test import TestCase
from django.urls import reverse
from .models import Book, Author
from .views import books_view, authors_view  # Додайте імпорт ваших вьюшок


class BooksViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Створити 6 книг для тесту
        number_of_books = 6
        for book_id in range(number_of_books):
            Book.objects.create(
                title=f'Book {book_id}',
                publication_date='2024-01-01',  # Встановлення однакової дати публікації для всіх книг
                price=10.00,
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('books/')  # Виправлено шлях
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('books'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('books'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books_list.html')

    def test_lists_latest_books(self):
        response = self.client.get(reverse('books'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('books' in response.context)
        self.assertEqual(len(response.context['books']), 5)


class AuthorsViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Створити 3 авторів та додати кожному по дві книги
        author1 = Author.objects.create(name='Author 1', bio='Bio 1')
        author2 = Author.objects.create(name='Author 2', bio='Bio 2')
        author3 = Author.objects.create(name='Author 3', bio='Bio 3')

        book1 = Book.objects.create(title='Book 1', publication_date='2024-01-01', price=10.00)
        book2 = Book.objects.create(title='Book 2', publication_date='2024-01-01', price=10.00)
        book3 = Book.objects.create(title='Book 3', publication_date='2024-01-01', price=10.00)

        author1.book_set.add(book1, book2)
        author2.book_set.add(book2, book3)
        author3.book_set.add(book3)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/authors/')  # Виправлено шлях
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('authors'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('authors'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authors.html')

    def test_lists_authors_with_book_count(self):
        response = self.client.get(reverse('authors'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('authors' in response.context)
        self.assertEqual(len(response.context['authors']), 3)
        for author in response.context['authors']:
            self.assertTrue('num_books' in author)
            self.assertTrue(author.num_books > 0)

class AuthorsViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Створити 3 авторів та додати кожному по дві книги
        author1 = Author.objects.create(name='Author 1', bio='Bio 1')
        author2 = Author.objects.create(name='Author 2', bio='Bio 2')
        author3 = Author.objects.create(name='Author 3', bio='Bio 3')

        book1 = Book.objects.create(title='Book 1', publication_date='2024-01-01', price=10.00)
        book2 = Book.objects.create(title='Book 2', publication_date='2024-01-01', price=10.00)
        book3 = Book.objects.create(title='Book 3', publication_date='2024-01-01', price=10.00)

        author1.book_set.add(book1, book2)
        author2.book_set.add(book2, book3)
        author3.book_set.add(book3)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('authors/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('authors'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('authors'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authors.html')

    def test_lists_authors_with_book_count(self):
        response = self.client.get(reverse('authors'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('authors' in response.context)
        self.assertEqual(len(response.context['authors']), 3)
        for author in response.context['authors']:
            self.assertTrue('num_books' in author)
            self.assertTrue(author.num_books > 0)

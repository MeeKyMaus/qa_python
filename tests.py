import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
class TestBooksCollector:

    # тестируем метод add_new_book с добавлением двух книг
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две книги
        assert len(collector.get_books_genre()) == 2

    # параметризация для тестирования set_book_genre
    @pytest.mark.parametrize(
        "book_name, genre, expected_genre", [
            ('Гордость и предубеждение и зомби', 'Фантастика', 'Фантастика'),
            ('Что делать, если ваш кот хочет вас убить', 'Комедии', 'Комедии'),
        ]
    )
    def test_set_book_genre(self, book_name, genre, expected_genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)

        assert collector.get_book_genre(book_name) == expected_genre

    # Тест для get_book_genre
    def test_get_book_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')

        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Фантастика'

    # Тест для get_books_with_specific_genre
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')

        books = collector.get_books_with_specific_genre('Фантастика')

        assert 'Гордость и предубеждение и зомби' in books

    # Тест для get_books_genre
    def test_get_books_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')

        books_genre = collector.get_books_genre()

        assert 'Гордость и предубеждение и зомби' in books_genre

    # Тест для get_books_for_children
    def test_get_books_for_children(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')

        children_books = collector.get_books_for_children()

        assert 'Гордость и предубеждение и зомби' in children_books

    # Тест для add_book_in_favorites
    def test_add_book_in_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        assert 'Гордость и предубеждение и зомби' in collector.get_list_of_favorites_books()

    # Тест для delete_book_from_favorites
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')

        assert 'Гордость и предубеждение и зомби' not in collector.get_list_of_favorites_books()

    # Тест для get_list_of_favorites_books
    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        favorites_books = collector.get_list_of_favorites_books()

        assert 'Гордость и предубеждение и зомби' in favorites_books

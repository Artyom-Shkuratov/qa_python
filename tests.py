from main import BooksCollector
import pytest

class TestBooksCollector:
    
    def test_add_new_book_two_books_added_successfully(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_set_book_genre_valid_book_and_genre_genre_updated_successfully(self, collector):
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        assert collector.get_book_genre('Шерлок Холмс') == 'Детективы'
        
    @pytest.mark.parametrize('book_name, genre', [('Гарри Поттер ', 'Фантастика'), ('Оно', 'Ужасы')])
    def test_set_book_genre_parametrize_correct_genre_assigned(self, collector, book_name, genre):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre
    
    def test_get_books_for_children_valid_books_filters_out_restricted(self, collector, filled_collector):
        children_books = filled_collector.get_books_for_children()
        assert "Гарри Поттер" in children_books
        assert "Колобок" in children_books
        assert "Оно" not in children_books
        
    def test_add_new_book_empty_name_book_not_added(self, collector):
        collector.add_new_book('') 
        assert '' not in collector.get_books_genre()
   
    def test_get_books_with_specific_genre_invalid_genre_returns_empty_list(self, collector):
        collector.add_new_book('Властелин Колец')
        collector.set_book_genre('Властелин Колец', 'Фантастика')
        result = collector.get_books_with_specific_genre('Драмма')
        assert result == []
        
    def test_add_book_in_favorites_valid_book_book_added_successfully(self, collector):
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        result = collector.get_books_for_children()
        assert 'Оно' not in result

    def test_add_book_in_favorites_duplicate_book_not_added(self, collector):
        collector.add_new_book('Оно')
        collector.add_book_in_favorites('Оно')
        assert "Оно" in collector.get_list_of_favorites_books(), 'Книга не добавлена!'
        
    def test_delete_book_from_favorites_existing_book_removed_successfully(self, collector):
        collector.add_new_book("Дюна")
        collector.add_book_in_favorites("Дюна")
        collector.add_book_in_favorites("Дюна")
        assert collector.get_list_of_favorites_books().count("Дюна") == 1
        
    def test_get_list_of_favorites_books_valid_books_returns_correct_list(self, collector):
        collector.add_new_book("Война и мир")
        collector.add_book_in_favorites("Война и мир")
        collector.delete_book_from_favorites("Война и мир")
        assert "Война и мир" not in collector.get_list_of_favorites_books()
        
    def test_get_list_of_favorites_books_returns_correct_list(self, collector):
        collector.add_new_book('Ночной дозор')
        collector.add_book_in_favorites('Ночной дозор')
        result = collector.get_list_of_favorites_books()
        assert 'Ночной дозор' in result

    def test_get_books_genre_valid_book_returns_correct_mapping(self, collector):
        collector.add_new_book('Пила')
        collector.set_book_genre('Пила', 'Ужасы')
        assert collector.get_books_genre() == {"Пила": "Ужасы"}

import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()


@pytest.fixture
def filled_collector():
    collector = BooksCollector()
    collector.add_new_book("Гарри Поттер")
    collector.set_book_genre("Гарри Поттер", "Фантастика")

    collector.add_new_book("Оно")
    collector.set_book_genre("Оно", "Ужасы")

    collector.add_new_book("Колобок")
    collector.set_book_genre("Колобок", "Мультфильмы")

    return collector    


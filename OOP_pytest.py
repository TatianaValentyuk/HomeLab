import pytest
from OOP import Book

@pytest.fixture
def book_list():
    books = [
            Book("Программист-прагматик. Путь от подмастерья к мастеру»", "Дэйв Томас", "Спектр", 1999, 250, 30.5,
                 "твердая обложка"),
            Book("Говорят, в IT много платят", "Елена Правдина", "Эксмо", 2021, 150, 25, "мягкая обложка"),
            Book("Путь программиста: человек эпохи IT", "Джон Сомнез", "Спектр", 2016, 421, 50, "твердая обложка"),
            Book("Код: тайный язык информатики", "Чарльз Петцольд", "АСТ", 2009, 290, 40, "мягкая обложка"),
            Book("Путь программиста: человек эпохи IT", "Джон Сомнез", "Спектр", 2016, 421, 50, "твердая обложка"),
            Book("Путь программиста: человек эпохи IT", "Джон Сомнез", "Спектр", 2015, 421, 50, "твердая обложка")
        ]

    return books


def test_init_(book_list):
    assert book_list[0].get_title() == 'Программист-прагматик. Путь от подмастерья к мастеру»'


def test_get_title(book_list):
    for book in book_list:
        assert book.get_title() == book.title
        assert book.get_author() == book.author
        assert book.get_publisher() == book.publisher

def test_author_update(book_list):
    for book in book_list:
        if book.price == 421:
            book.set_price = 455
            assert book.get_price() !=book.price

def test_list_author(book_list):
    for book in book_list:
        if book.author == "Джон Сомнез":
            assert book.get_author() == "Джон Сомнез"



if __name__ == '__main__':
    pytest.main()
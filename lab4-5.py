#KлассKласс Book: id, Название, Автор (ы), Издательство, Год издания, Количество страниц, Цена, Тип переплета.
#Функции-члены реализуют запись и считывание полей (проверка корректности).
#Создать список объектов. Вывести:
#a)	список книг заданного автора;
#б) список книг, выпущенных после заданного года.
# Book: id, Название, Автор (ы), Издательство, Год издания, Количество страниц, Цена, Тип переплета.
#Функции-члены реализуют запись и считывание полей (проверка корректности).
#Создать список объектов. Вывести:
#a)	список книг заданного автора;
#б) список книг, выпущенных после заданного года.

import uuid
import random
# Класс реализующий Book
class Book(object):
    __id = 0  # приватное стат поле для хранения __id
    _name_author = {0: '_surname', 1: '_name'}

    # Метод инициализации создаваемого объекта класса Книга (заполнение информацией созданного в __new__ объекта)
    def __init__(self, title, author, publisher, year, pages, price, type_cover):
        self.__id = uuid.uuid4()
        Book.__id += 1 #увел. кол-во книг при создании каждого экз класса
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year
        self.pages = pages
        self.price = price
        self.type_cover = type_cover

        # Метод создания объекта класса Book
    def __new__(cls, title, author, publisher, year, pages, price, type_cover):
        # Вывод на консоль сообщения о начале создания объекта Book
        print("Удачно..")
        # Проверка параметров конструктора на соответствие нужным типам данных
        # author должен быть строковым типом (str)
        # year должен быть целым числом (int)
        if not isinstance(author, str) or not isinstance(year, int):
            # Сообщение о несоответствии типов данных и прекращении создании объекта
            print("Неудачно. Предоставлена неверная информация!")
            # Возвращаем None в качестве результата при неудачном создании
            # Для этого случая метод __init__ вызван не будет
            return None
        instance = object.__new__(cls)
        if year > 0 and pages > 0:
            return instance
        else:
            return None


    @classmethod
    def get_id_count(cls):
        print("Кол-во книг в каталоге:")
        return cls.__id

    def get_title(self):
        return self.title
    def set_title(self, title):
        self.title = title
    def get_author(self):
        return self.author
    def set_author(self, author):
        self.author = author
    def get_publisher(self):
        return self.publisher
    def get_year(self):
        return self.year
    def get_pages(self):
        return self.pages
    def get_price(self):
        return self.price
    def get_type_cover(self):
        return self.type_cover

books = [
    Book("Программист-прагматик. Путь от подмастерья к мастеру»", "Дэйв Томас", "Спектр", 1999, 250, 30.5, "твердая обложка"),
    Book("Говорят, в IT много платят", "Елена Правдина", "Эксмо", 2021, 150, 25, "мягкая обложка"),
    Book("Путь программиста: человек эпохи IT", "Джон Сомнез", "Спектр",  2016, 421, 50, "твердая обложка"),
    Book("Код: тайный язык информатики", "Чарльз Петцольд", "АСТ", 2009, 290, 40, "мягкая обложка"),
    Book("Путь программиста: человек эпохи IT", "Джон Сомнез", "Спектр", 2016, 421, 50, "твердая обложка"),
    Book("Путь программиста: человек эпохи IT", "Джон Сомнез", "Спектр", 2015, 421, 50, "твердая обложка")
   ]

def list_books(books):
        print("Список книг:")
        for book in books:
            print(f"{book.get_title()}, {book.get_author()}, {book.get_publisher()}")


def list_author(author):
    print("Список книг автора  " + author)
    for book in books:
        if book.get_author() == author:
            print(f"{book.get_title()}, {book.get_author()}, {book.get_publisher()}")

def list_year(year):
    print("Список книг, выпущенных после " + f"{year}")
    for book in books:
        if book.get_year() >= year:
            print(f"{book.get_title()}, {book.get_author()}, {book.get_year()}")

list_books(books)
list_author("Джон Сомнез")
list_year(2014)
print(Book.get_id_count())


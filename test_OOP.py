import unittest
from OOP import Book

class MyBookTestCase(unittest.TestCase):
    book1 = None
    books = []

    @classmethod
    def setUpClass(cls):
        """Set Up Class Method!"""
        print("Starting tests for Book Class..")
        books = [
            Book("Программист-прагматик. Путь от подмастерья к мастеру»", "Дэйв Томас", "Спектр", 1999, 250, 30.5,
                 "твердая обложка"),
            Book("Говорят, в IT много платят", "Елена Правдина", "Эксмо", 2021, 150, 25, "мягкая обложка"),
            Book("Путь программиста: человек эпохи IT", "Джон Сомнез", "Спектр", 2016, 421, 50, "твердая обложка"),
            Book("Код: тайный язык информатики", "Чарльз Петцольд", "АСТ", 2009, 290, 40, "мягкая обложка"),
            Book("Путь программиста: человек эпохи IT", "Джон Сомнез", "Спектр", 2016, 421, 50, "твердая обложка"),
            Book("Путь программиста: человек эпохи IT", "Джон Сомнез", "Спектр", 2015, 421, 50, "твердая обложка")
        ]


    @classmethod
    def tearDownClass(cls):
        """Tear Down Class Method!"""
        print("End tests for Book Class!")



    def setUp(self):
        """Set Up Method!"""
        #print("Initialize book for [" + self.shortDescription() + "]")
        self.book1 = Book("Программист-прагматик. Путь от подмастерья к мастеру»", "Дэйв Томас", "Спектр", 1999, 250, 30.5, "твердая обложка")
        self.book2 = Book("Говорят, в IT много платят", "Елена Правдина", "Эксмо", 2021, 150, 25, "мягкая обложка")

    def test__init__(self):
        """Init Method!"""
        self.assertEqual(self.book1.get_title(), "Программист-прагматик. Путь от подмастерья к мастеру»")
        self.assertEqual(self.book1.get_author(), "Дэйв Томас")
        self.assertEqual(self.book1.get_publisher(), "Спектр")
        self.assertEqual(self.book1.get_year(), 1999)
        self.assertEqual(self.book1.get_pages(), 250)
        self.assertEqual(self.book1.get_price(), 30.5)
        self.assertEqual(self.book1.get_type_cover(), "твердая обложка")

    def test_set_author(self):
        """set_author Method!"""
        self.assertEqual(self.book1.get_author(), "Дэйв Томас")
        self.book1.set_author("Д.Томас")
        self.assertEqual(self.book1.get_author(), "Д.Томас")
        self.book1.set_author("Дэйв Томас")


    def test_price_greater(self):
        self.assertGreater(self.book1.get_price(), self.book2.get_price())

    def test_title_instance(self):
        self.assertIsInstance(self.book1.get_title(), str)

    def test_book_equal(self):
        self.assertNotEqual(self.book1, self.book2)

    def test_str(self):
        """str Method!"""
        self.assertIn(str(self.book2.get_year()), str(202120))

    def test_list_books(self):
        for self.book in self.books:
           print("The Titles match ")
           self.assertEqual(self.book.get_title(), self.book.title)














if __name__ == '__main__':
    unittest.main()

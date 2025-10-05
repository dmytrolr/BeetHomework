class Library:
    def __init__(self, name: str):
        self.name = name
        self.books = []
        self.authors = []

    def __repr__(self):
        return f"Library({self.name!r}, books={len(self.books)}, authors={len(self.authors)})"

    def __str__(self):
        return f"Library {self.name!r}: {len(self.books)} books, {len(self.authors)} authors"

    def new_book(self, name: str, year: int, author: "Author") -> "Book":
        if not isinstance(author, Author):
            raise TypeError("author must be an Author instance")
        book = Book(name, year, author)
        self.books.append(book)
        if author not in self.authors:
            self.authors.append(author)
        return book

    def group_by_author(self, author: "Author") -> list:
        return [b for b in self.books if b.author is author]

    def group_by_year(self, year: int) -> list:
        return [b for b in self.books if b.year == year]


class Book:
    book_count = 0

    def __init__(self, name: str, year: int, author: "Author"):
        if not isinstance(author, Author):
            raise TypeError("author must be an Author instance")
        self.name = name
        self.year = year
        self.author = author

        Book.book_count += 1
        author.books.append(self)

    def __repr__(self):
        return f"Book({self.name!r}, {self.year}, author={self.author.name!r})"

    def __str__(self):
        return f"'{self.name}' ({self.year}) by {self.author.name}"


class Author:
    def __init__(self, name: str, country: str, birthday: str):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return (
            f"Author({self.name!r}, {self.country!r}, birthday={self.birthday!r})"
        )

    def __str__(self):
        return f"{self.name} from {self.country}, born {self.birthday}"

# if __name__ == "__main__":
#     a1 = Author("Тарас Шевченко", "Ukraine", "1814-03-09")
#     a2 = Author("Леся Українка", "Ukraine", "1871-02-25")
#     a3 = Author("Іван Франко", "Ukraine", "1856-08-27")
#     a4 = Author("Ліна Костенко", "Ukraine", "1930-03-19")
#     a5 = Author("Григорій Сковорода", "Ukraine", "1722-12-27")
#
#     a6 = Author("William Shakespeare", "England", "1564-04-26")
#     a7 = Author("Johann Wolfgang von Goethe", "Germany", "1749-08-28")
#     a8 = Author("Dante Alighieri", "Italy", "1265-06-01")
#     a9 = Author("Victor Hugo", "France", "1802-02-26")
#     a10 = Author("Miguel de Cervantes", "Spain", "1547-09-29")
#     a11 = Author("Franz Kafka", "Czech Republic", "1883-07-03")
#     a12 = Author("Adam Mickiewicz", "Poland", "1798-12-24")
#     a13 = Author("Wisława Szymborska", "Poland", "1923-07-02")
#     a14 = Author("Hans Christian Andersen", "Denmark", "1805-04-02")
#     a15 = Author("Albert Camus", "France", "1913-11-07")
#     a16 = Author("José Saramago", "Portugal", "1922-11-16")
#     a17 = Author("Selma Lagerlöf", "Sweden", "1858-11-20")
#     a18 = Author("Elias Canetti", "Bulgaria", "1905-07-25")
#
#     lib = Library("City Library")
#
#     lib.new_book("Kobzar", 1840, a1)
#     lib.new_book("Лісова пісня", 1911, a2)
#     lib.new_book("Захар Беркут", 1883, a3)
#     lib.new_book("Марія Чурай", 1976, a4)
#     lib.new_book("Нарцис і Золото", 1788, a5)
#
#     lib.new_book("Hamlet", 1603, a6)
#     lib.new_book("Faust", 1808, a7)
#     lib.new_book("The Divine Comedy", 1320, a8)
#     lib.new_book("Les Misérables", 1862, a9)
#     lib.new_book("Don Quixote", 1605, a10)
#     lib.new_book("The Trial", 1925, a11)
#     lib.new_book("Pan Tadeusz", 1834, a12)
#     lib.new_book("View with a Grain of Sand", 1996, a13)
#     lib.new_book("Fairy Tales", 1835, a14)
#     lib.new_book("The Stranger", 1942, a15)
#     lib.new_book("Blindness", 1995, a16)
#     lib.new_book("The Wonderful Adventures of Nils", 1906, a17)
#     lib.new_book("Crowds and Power", 1960, a18)
#
#     print(lib)
#     print(a1.books)
#     print(Library.group_by_year(lib, 1605))
#     print(Book.book_count)

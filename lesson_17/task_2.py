class Author:
    def __init__(self, name: str, country: str, birthday: str):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def books_count(self):
        return len(self.books)

    def __str__(self):
        return f"Author name: {self.name}, country: {self.country}, birthday: {self.birthday}"

    def __repr__(self):
        return repr(
            f"Author name: {self.name}, country: {self.country}, birthday: {self.birthday}"
        )


class Book:
    count = 0

    def __init__(self, name: str, year: int, author: Author):
        self.name = name
        self.year = year
        self.author = author
        self.author.add_book(self)

        Book.count += 1

    def __del__(self):
        Book.count -= 1

    def __str__(self):
        return f"Book name: {self.name}, year: {self.year}, author: {self.author.name}"

    def __repr__(self):
        return repr(
            f"Book name: {self.name}, year: {self.year}, author: {self.author.name}"
        )


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name: str, year: int, author: Author):
        book = Book(name, year, author)

        self.books.append(book)
        self.authors.append(author)

        return book

    def group_by_author(self, author: Author):
        return list(filter(lambda book: book.author is author, self.books))

    def group_by_year(self, year: int):
        return list(filter(lambda book: book.year == year, self.books))

    def __str__(self):
        return f"Library name: {self.name}\n<Books>\n{self.books}\n<Authors>\n{self.authors}"

    def __repr__(self):
        return repr(
            f"Library name: {self.name}, Books count: {len(self.books)}, Authors count: {len(self.authors)}"
        )


library = Library("Admont Abbey Library")
salinger = Author("Jerome David Salinger", "USA", "January 1, 1919")
reid = Author("Thomas Mayne Reid", "Irland", "22 October 1883")

library.new_book("The Catcher in the Rye", 1951, salinger)
library.new_book("Franny and Zooey", 1961, salinger)
library.new_book("The White Chief; A Legend of North Mexico", 1853, reid)
library.new_book(
    "The Boy Hunters, or, Adventures in Search of a White Buffalo", 1856, reid
)
library.new_book("The Lone Ranch", 1860, reid)
library.new_book("The Scalp Hunters", 1860, reid)


assert Book.count == 6
assert salinger.books_count() == 2
assert reid.books_count() == 4
assert len(library.group_by_author(salinger)) == 2
assert len(library.group_by_author(reid)) == 4
assert len(library.group_by_year(1860)) == 2

print(library, end="\n")
print(library.group_by_author(salinger))
print(library.group_by_author(reid))

print(repr(library))

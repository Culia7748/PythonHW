from book import Book

library = [
    Book("Война и мир", "Толстой Л.Н."),
    Book("Капитанская дочка", "Пушкин А.С."),
    Book("Ромео и Джульета", "В.Шекспир")
]

for book in library:
    print(f"{book.name} - {book.autor}")
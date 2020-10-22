class Library:
    def __init__(self, Name):
        self.Name = Name
        self.Library = list()

    def add(self, book):
        
        if book not in self.Library:
            self.Library.append(book)

        else:
            print(f'{book.Title} is already in the {self.Name}')
    
    def search(self, author):
        control = False
        for books in self.Library: 
            if author in list(books.Book.values())[0]:
                control = True
                print(author, ':', books.Title) 
        
        if not control:
            print(f'There no books of {author} in the {self.Name}') 
        

    def info(self, searched_book):
        for book in self.Library: 
            if book.Title == searched_book:
                print(searched_book, ":", ', '.join(book.Book[searched_book]))
                break
        else:
            print(f'The book {searched_book} is not found in the {self.Name}') 
    
    def remove(self, book):
        self.Library = self.Library[1::]

class Book:
    def __init__(self, Title, Author, Publisher, Release, ISBN):
        self.Book = dict()
        self.Title = Title
        self.Author = Author
        self.Publisher = Publisher
        self.Release = Release
        self.ISBN = ISBN
        self.Book[self.Title]= [self.Author, self.Publisher, self.Release, self.ISBN]
        print()

   
def test_library():
    Some_Interesting_Place = Library('Some_Interesting_Place')
    book1 = Book("War and Peace", "Tolstoy Leo", "PUBLISHER", "2010", "3456-4567-567")
    book2 = Book("Anna Karenina", "Tolstoy Leo", "PUBLISHER-1", "2011", "3456-4567-797")
    book3 = Book("Heart of a Dog", "Mikhail Bulgakov", "PUBLISHER-2", "2001", "0000-0000-797")

    
    Some_Interesting_Place.add(book1)
    Some_Interesting_Place.add(book1)
    Some_Interesting_Place.add(book2)
    
    Some_Interesting_Place.search('Mikhail Bulgakov')
    Some_Interesting_Place.search('Tolstoy Leo')
    
    Some_Interesting_Place.info("Anna Karenina")
    Some_Interesting_Place.info("Heart of a Dog")

   
    for book in Some_Interesting_Place.Name:
         Some_Interesting_Place.remove(book)
    print(Some_Interesting_Place.Library)

if __name__ == '__main__':
    test_library()

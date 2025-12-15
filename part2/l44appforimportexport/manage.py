from book import Book 

class BookManage:
    def __init__(self):
        self.books = []
    
    def addbook(self,title,author,year):
        newbook = Book(title,author,year)
        self.books.append(newbook)
        print(f"New Book Created : {title}")

    def listbooks(self):
        print("All Book list :")
        for idx,book in enumerate(self.books): # start=1
            # print(f"{idx}. {book.bookinfo()}")
            print(f"{idx+1}. {book.bookinfo()}")

    def searchbyauthor(self,author):
        return [book for book in self.books if book.author.lower() == author.lower()]
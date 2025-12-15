from models.book import Book 
from models.user import User
from models.utilities import *

def main():
    bookObj1 = Book("Python","Daw Win Win",20,500)
    bookObj2 = Book("Django","Daw Tun Tun",40,800)
    bookObj3 = Book("Open AI","Daw Hnin Hnin",50,1000)

    # original
    # discount 

    specialdiscount(bookObj1)
    specialdiscount(bookObj2)

    # user
    user = User("Yamin")
    user.addtocart(bookObj1)
    user.addtocart(bookObj2)
    user.addtocart(bookObj3)

    print("Book Titles : ", gettitles(user.carts))
    print(f"Total pages in book 1 = {len(bookObj1)}")
    print(f"Total pages in book 2 = {len(bookObj2)}")

    print(user)

    print(f"Total price : {user.totalprice():.3f} ")

    

if __name__ == "__main__":
    main()

# Book 
# User

# Original Price : 100 10% 
# After Dis Price : 90
# Book Title: [,,,]
# book 1 pages : 10
# book 2 pages : 15
# book 3 pages : 15
# User: Su Su , Card : ['Story One by nu nu','Story Two by u bu']
# Total Price : 90 
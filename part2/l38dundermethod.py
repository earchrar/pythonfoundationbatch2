# => Dunder Methods 
# => __len__ , __add__ 

from typing import Self

class Article: 
    def __init__(self,title:str,rating:int) -> None:            # Dunder Methods 
        self.title = title 
        self.rating = rating 

    def __len__(self) -> int:                                   # Dunder Methods 
        return self.rating 
    
    def __add__(self,other:Self) -> Self:
    # def __add__(self,other:set) -> set:                       # Dunder Methods 
        combinedtitle:str = f'{self.title} & {other.title}'
        combinedrating:int = self.rating + other.rating
        return Article(combinedtitle,combinedrating)

def main() -> None:                                             # function , outside of the class 
    sport: Article = Article('This is sport article',3)
    news: Article = Article('This is news article',5)

    print(sport.title) # This is sport article.
    print(len(sport)) # 3

    print(news.title) # This is new article.
    print(len(news)) # 5

    mixarticles: Article =  sport + news 
    print(mixarticles)
    print(mixarticles.title)
    print(mixarticles.rating)

if __name__ == "__main__":
    main()

# => Object Comparison 
# __eq__ , equality
# __lt__ , less than 
# __gt__ , greater than 


from typing import Self 

class Mobile: 
    def __init__(self,brand:str,price:int,color:str) -> None:
        self.brand = brand 
        self.price = price 
        self.color = color  

    # def __eq__(self,other:Self) -> bool:    # check only 1 parameter 
    #     return self.price == other.price 

    def __eq__(self,other:Self) -> bool:    # check all parameters 
        print("Current = ",self.__dict__)
        print("Other = ",other.__dict__)
        return self.__dict__ == self.__dict__
    
    def __lt__(self,other:Self) -> bool: 
        return self.price == other.price 
    
    def __gt__(self,other:Self) -> bool: 
        return self.price == other.price 

def main() -> None:                         # function , outside of the class

    mob1: Mobile = Mobile('Oppo',300,'blue')
    mob2: Mobile = Mobile('Oppo',400,'blue')

    print(mob1) # <__main__.Mobile object at 0x000001F61E439400>
    print(mob2) # <__main__.Mobile object at 0x000001F61E3B5E50>
    print(mob1 == mob2) # before eq , True after eq
    print(mob1 < mob2) # False 
    print(mob1 > mob2) # False

if __name__ == "__main__":
    main()

# __str__ = string 
# __repr__ = representation 

class Person: 
    def __init__(self,name:str,age:int) -> None: 
        self.name = name 
        self.age = age 

    # def __repr__(self) -> str: 
    def __str__(self) -> str:
        return f'Name is {self.name}. {self.age} years old.'

def main() -> None: 

    personObj: Person = Person("Hnin Hnin",25)
    print(personObj) # before repr , <__main__.Person object at 0x0000019DABB3D400> , after repr Name is Hnin Hnin. 25 years old.
    print(repr(personObj)) # Name is Hnin Hnin. 25 years old. , with str <__main__.Person object at 0x0000026257B3D400>

if __name__ == "__main__":
    main()

# => indexing
# __getitem__

class Worker: 
    def __init__(self,names:str) -> None: 
        self.names = names 

    def __getitem__(self,index): 
        return self.names[index]
    
def main() -> None: 

    workerObj: Worker = Worker(["Aung Aung","Tun Tun","Kyaw Kyaw"])
    print(workerObj[0]) # Aung Aung
    print(workerObj[1]) # Tun Tun
    print(workerObj[2]) # Kyaw Kyaw

if __name__ == "__main__":
    main()

# => Deleting an Object 
# __del__

class People: 
    def __init__(self,name) -> None: 
        self.name = name 

    def __del__(self): 
        print(f'{self.name} has been deleted.')
    
def main() -> None: 

    peopleObj: People = People("Linn Linn")
    del peopleObj # Linn Linn has been deleted.

if __name__ == "__main__":
    main()


# dundermethod.py
    # __init__
    # __len__
    # __add__

    # Object Comparsion 
    # __eq__
    # __lt__
    # __gt__

    # representation
    # __str__
    # __repr__

    # indexing
    # __getitem__

    # Deleting an Object
    # __del__


        

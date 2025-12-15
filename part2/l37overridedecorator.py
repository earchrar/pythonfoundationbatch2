# => Override Decorator 

# exe 

class Animal:
    datas: list[str] = []   # Properties , Attributes 

    def __init__(self,name:str) -> None: 
        self.name = name
    
    def task(self,todo:str) -> None:
        self.datas.append(todo)

def main() -> None: 
    cat: Animal = Animal("Cat")
    dog: Animal = Animal("dog")

    cat.task('sleep')
    cat.task('eat')
    print(cat.datas) # ['sleep', 'eat']

    dog.task('run')
    dog.task('watch')
    print(dog.datas) # ['sleep', 'eat', 'run', 'watch']

if __name__ == "__main__":
    main()

# => Override Decorator 

# => exe without Override Decorator 

class Parent1:
    def greet(self) -> None:
        print("Hello from Parent 1!")

class Child1(Parent1):
    def greett(self) -> None: 
        print("Hello from Child 1!")

Child1().greet() # Hello from Parent 1!

# => exe with Override Decorator ( @override , python3 version = 3.13.9 )

from typing import override 

class Parent2:
    def greet(self) -> None:
        print("Hello from Parent 2!")

class Child2(Parent2):
    @override
    def greet(self) -> None: 
        print("Hello from Child 2!")

Child2().greet() # Hello from Child 2!

# exe 

from typing import override 

class Shape: 
    def __init__(self,name:str,slides:int) -> None:
        self.name = name
        self.slides = slides 

    def describe(self) -> None:
        print(f'{self.name} have {self.slides} slides')

    def info(self) -> None: 
        print(f'this is {self.name} info method.') 

class Square(Shape):
    def __init__(self,size:float) -> None:
        super().__init__("Square",4)
        self.size = size

    @override
    def info(self) -> None: 
        print(f'this is {self.name} info method with a shape of {self.size}') 

class Reactangle(Shape):
    def __init__(self,width:float,height:float) -> None:
        super().__init__("Reactangle",4)
        self.width = width 
        self.height = height

    @override
    def info(self) -> None: 
        print(f'this is {self.name} info method with area of ({self.width} x {self.height})') 

def main() -> None: 

    square: Square = Square(10)
    square.describe()
    square.info()

    square: Reactangle = Reactangle(30,40)
    square.describe()
    square.info()

if __name__ == "__main__":
    main()





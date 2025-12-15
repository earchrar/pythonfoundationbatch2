class Car:                                             # defining the class               
    def __init__(self,brand:str,wheels:int,) -> None:  # this constructor __int__() type hint 
        self.brand = brand                             # public attribute 
        self._wheels = wheels                          # protected attribute 
        self.__enginestatus = False                    # private attribute

    def engineon(self) -> None: 
        self.__enginestatus = True  
        print(f'Engine on : {self.brand}')             # Instance Public Methods

    def engineoff(self) -> None: 
        self.__enginestatus = False  
        print(f'Engine off : {self.brand}')

    def drive(self,km:float) -> None: 
        if self.__enginestatus: 
            print(f'Diving : {self.brand} for {km}km/h')
        else:
            print(f'Cannot Drive : {self.brand} engine is off!')

    def describe(self) -> None: 
        print(f'{self.brand} is a car with {self._wheels} wheels')

    def __checkcomputerbox(self) -> None:                       # Instance Private Methods
        print(f'Checking Computer Box of {self.brand}')

    def _serviceengine(self) -> None:                           # Instance Protected Methods
        print(f'Servicing the engine of {self.brand}')

    def maintenance(self) -> None:                              # Instance Public Methods (as getter)
        print(f'Maintenance on {self.brand}!')
        self.__checkcomputerbox()
        self._serviceengine()

def main() -> None: 
    toyota: Car = Car('Toyota',4)
    toyota.engineon()
    toyota.drive(50)
    toyota.engineoff()
    toyota.describe()

    # print(f'This is protected atribute = {toyota._wheels}') # not recommended This is protected atribute = 4
    # print(f'This is private atribute = {toyota.__enginestatus}') # error 
    # print(f'This is private atribute = {toyota._Car__enginestatus}') # not recommended This is private atribute = False

    # toyota._serviceengine() # not recommended
    # toyota.__checkcomputerbox() # error 
    # toyota._Car__checkcomputerbox() # not recommended

    toyota.maintenance()

if __name__ == "__main__":
    main()

# Modifier          Syntax              Access Inside Class               Access Inside Subclass              Access Outside Class
# Public            self.name                 Yes                              Yes                                   Yes
# Private           self.__name               Yes                              NO                                    Yes
# Protected         self._name                Yes                              Yes                              Possible (shoud not use)
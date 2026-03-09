'''

Abstraction:
    Hiding the internal implementation and showing only the functionality to the end user.

Abstract Method:
    If a method or a function consists of only declarationnot definition then it will be called as "Abstract Method".

Abstract Class:
    If a class consists of atleast one abstract method, then it will be called as "Abstract Class".

Concrete Class:
     If a class consists of zero abstract method, it will be known as concrete class.

abc: Module
ABC: Abstract Base Class
'''

from abc import ABC, abstractmethod

class ATM(ABC):        ##Abstract Class
    @abstractmethod
    def generate_pin(self):
        pass

    @abstractmethod
    def forget_pin(self):
        pass

    @abstractmethod
    def check_bal(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass

    @abstractmethod
    def deposit(self):
        pass

class SBI_ATM(ATM):     ## Concrete class
    
    def generate_pin(self):
        print('It is used to generate ATM pin!')

    def forget_pin(self):
        print('Forgot Password!')
    
    def check_bal(self):
        print('No Balance is there')

    def deposit(self):
        print('Save my money in my account')
    
    def withdraw(self):
        print('Do not withdraw the Money! PLlease!')

obj = SBI_ATM()
obj.generate_pin()
obj.check_bal()
obj.forget_pin()
obj.deposit()
obj.withdraw()
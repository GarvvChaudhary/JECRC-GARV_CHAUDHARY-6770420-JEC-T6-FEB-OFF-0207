## INHERITANCE

'''
1. Single level Inheritance
2. Multi level Inheritance
3. Multiple Inheritance
4. Hierarchical Inheritance
5. Hybrid Inheritance
'''

## Single level Inheritance
## We will have a single parent and a single child class. Also the properties will be derived only one time.

## Parent class or, Super class
## The classs from which we are going to derive the properties is known as Parent class.
class Parent:
    bank_balance = '54L'

    def __init__(self, members):
        self.members = members

    def description(self):
        print('I am the parent class.')

## Child class or, Sub class
## The class in which we are going to derive the properties is known as Child class.
class Child(Parent):
    def __init__(self, child_name, *args):
        self.child_name = child_name
        super().__init__(args)
        
    def display(self):
        super().description()

obj = Child('Alice', 'Mom', 'Dad')
print(obj.members)
print(obj.child_name)
obj.display()
## constructor chaining: Calling parent class's constructor from inside child class's constructor is known as constructor chaining.


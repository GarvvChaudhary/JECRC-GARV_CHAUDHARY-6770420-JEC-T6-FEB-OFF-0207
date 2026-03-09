'''
Encapsulation:
    1. It is used to provide security to the data( data means variables/properties & methods present inside a class.)

How to provide security to the data?
    To provide security, we have to use access specifiers.
        1. public,
        2. protected,
        3. private,

Access Specifiers:
    It describes who can access the class members (properties & methods).
'''



## Example for public access specifier.
# class Temp:
#     a,b,*c,d = 'HELLO'

#     def greeting(self):
#         print('Good afternon user :)')

# class C2(Temp):
#     pass

## Protected Access Specifier:

# class Temp:
#     ## single underscore_ is known as soft barrier.

#     _a = 10
#     _b = 'I LOVE PYTHON !'

# obj = Temp()
# print(obj._b)  
# print(obj._a)

## Private Access Specifier:

# class Temp:
#     __a = 100

#     def __status(self):
#         print('Class name is Temp!')

# obj = Temp()
# # print(obj.__a)  
# # obj.__status()  

'''
1. by using Syntax,
2. get & set method,
3.  by using @property decorator(setter)
'''
## By usng Syntax
'''
obj_name/class_name._CN_prop_name/_method_name (Accessing)
obj_name/class_name._CN_MemberName = NewValue (Modifying)
'''

# print(obj._Temp__a)
# print(Temp._Temp__a)
# obj._Temp__status()


# def new_method():
#     print('Method is overridden')

# obj._Temp__a = '0123445678'
# obj._Temp__status = new_method
# print(obj._Temp__a)
# obj._Temp__status()





## By using get & set method

# class Temp:
#     __a = 100

#     def __status(self):
#         print('Class name is Temp!')
#     def get(self):
#         print(self.__a)
#     def set(self, new_val):
#         self.__a = new_val


# obj = Temp()
# obj.get()
# obj.set(1)
# obj.get()
# print(obj._Temp__a)



## By using @property decorator

class Temp:
    __a = 18

    @property
    def get(self):
        print(self.__a)

    @get.setter
    def set(self, new_val):
        self.__a = new_val

obj = Temp()
obj.get
obj.set = 45
obj.get
print(obj._Temp__a)
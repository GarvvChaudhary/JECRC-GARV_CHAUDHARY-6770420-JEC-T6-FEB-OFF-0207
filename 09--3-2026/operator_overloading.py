'''
-- Operator Overloading: It is a phenomenon of making the operators to work on user-defined data types by invoking respective magic methods.
-- Magic Method/Dundar: It is a special type of method in which double underscore __ will be there at the starting & ending of the method's name.

-- Example:
    1. __add__,
    2. __sub__,
    3. __mul__,
    4. __floordiv__,
    5. __truediv__,
    6. __mod__,

-- If we do not use operator overloading then what will happen?
    For using the operators inside user-defined data types we have to use operator overloading.

-- Syntax:
    class ClassName:
        def __init__(self, val):
            self.val = val
        
        def __add__ (self, ano_obj)
            return self.val + ano_obj.val

    obj1 = ClassName(val1)
    obj2 = ClassName(val2)
    print(obj1 + obj2)  ## obj1.__add__(obj2)
'''

class MyDT:
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return str(self.val)
## using packing we can perform addition of more than 2 numbers.

    # def __add__(self, ano_obj):
    #     return self.val + ano_obj.val
    
    def __add__(self, *ano_obj):
        sum = self.val
        for i in ano_obj:
            sum += i.val
        return MyDT(sum)
        

    # def add(self, *args):
    #     sum = self.val
    #     for i in args:
    #         sum += i.val
    #     return sum
    
    # def __sub__(self, ano_obj):
    #     return self.val - ano_obj.val
    
    def __sub__(self, *ano_obj):
        diff = self.val
        for i in ano_obj:
            diff -= i.val
        return MyDT(diff)
    
    # def sub(self, *args):
    #     diff = self.val
    #     for i in args:
    #         diff -= i.val
    #     return diff
    
    def __mul__(self, ano_obj):
        return self.val * ano_obj.val
    
    def mul(self, *args):
        product = self.val
        for i in args:
            product *= i.val
        return product
    
    def __mod__(self, ano_obj):
        return self.val % ano_obj.val
    
    def mod(self, *args):
        rem = self.val
        for i in args:
            rem %= i.val
        return rem
    
    def __floordiv__(self, ano_obj):
        return self.val // ano_obj.val
    
    def __truediv__(self, ano_obj):
        return self.val / ano_obj.val
        
        
        
# print(MyDT(100) + MyDT(20))
    
# print(MyDT.add(MyDT(100), MyDT(20), MyDT(30), MyDT(40), MyDT(500)))

print(MyDT(100) + MyDT(20) + MyDT(30) + MyDT(40) + MyDT(50))

# print(MyDT(100) - MyDT(20))
# print(MyDT.sub(MyDT(100), MyDT(20), MyDT(30), MyDT(40), MyDT(50)))

print(MyDT(100) - MyDT(20) - MyDT(30) - MyDT(40) - MyDT(50))

# print(MyDT(2) * MyDT(5))
# print(MyDT.mul(MyDT(2), MyDT(5), MyDT(10), MyDT(20), MyDT(30)))

# print(MyDT(100) // MyDT(20))


# print(MyDT(100) / MyDT(20))


# print(MyDT(100) % MyDT(20))

# print(MyDT.mod(MyDT(100), MyDT(20), MyDT(30), MyDT(40), MyDT(50)))

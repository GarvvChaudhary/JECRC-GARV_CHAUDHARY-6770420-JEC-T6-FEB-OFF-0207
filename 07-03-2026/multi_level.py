




class Class_1: ## parent
    a = 'class_1'

class Class_2(Class_1): ## parent
    b = 'class_2'

class Class_3(Class_2): ## child
    c = 'class_3'

class Class_4(Class_3): ## child
    d = 'class_4'

class Class_5(Class_4): ## child
    e = 'class_5'

obj = Class_5()
print(obj.a, obj.b, obj.c, obj.d, obj.e)
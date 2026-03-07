class Car:
    ## Below variables are known as "Properties/States/Members".
    wheelers = 4
    engine = 'Petrol'
    base_speed = '40kmph'
    max_speed = '120kmph'
    gears = 4
    
    def __init__(self, air_bags, security, base_budget, varient, total_sale):
        self.air_bags = air_bags
        self.security = security
        self.base_budget = base_budget
        self.varient = varient
        self.total_sale = total_sale
    
    @classmethod
    def update_gears(cls, new_gears):
        cls.gears = new_gears
        print(f'No of Gears: {cls.gears}')
    
    ## Functionality
    def display_properties(self):
        print({
            'wheelers': self.wheelers,
            'engine': self.engine,
            'base_speed': self.base_speed,
            'max_speed': self.max_speed,
            'gears': self.gears,
            'air_bags': self.air_bags,
            'security': self.security,
            'base_budget': self.base_budget,
            'varient': self.varient,
            'total_sale': self.total_sale
        })
    
    def update_base_speed(self, new_speed):
        self.base_speed = new_speed
        print(f'New Base Speed: {self.base_speed}')
        
    def update_max_speed(self, new_speed):
        self.max_speed = new_speed
        print(f'New Max Speed: {self.max_speed}')


TATA = Car(True, 'Level 5', '2L', 12, 100000)
print('Properties before updation:')
TATA.display_properties()
print()

print('Properties after updation:')
TATA.update_base_speed('60kmph')
TATA.update_max_speed('160kmph')
TATA.update_gears(5)
TATA.display_properties()



mahindra = Car(True, 'Level 4', '4L', 22, 250000)
print()
print('Mahindra: ')
mahindra.display_properties()



# self.prop_name

## constructor (__init__)

'''
class ClassName:
    properties
    
    def __init__(self, arg1, arg2, arg3, ..., argn):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        ...
        self.argn = argn
'''

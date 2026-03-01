# '''
# Problem: An electricity board charges consumers based on units consumed:

# First 100 units → ₹5 per unit

# Next 200 units → ₹7 per unit

# Above 300 units → ₹10 per unit

# Calculate total bill amount.
# '''

# unit = int(input("Units consumed: "))
# bill = None

# if unit > 0:

#         if unit <=100:
#             bill = unit *5
#         elif unit <=300:
#             bill = 100*5 + (unit-100)*7
#         elif unit >300:
#             bill = 100*5 + 200*7 + (unit-300)*10

#         if bill > 5000:
#             bill =  bill*0.95
# else:
#     print("Invalid unit consumed.")
      
# print("Total bill amount after discount is : ₹", bill)   

'''
Problem:
Loan approved if:
Salary > 25000
Cibil Score > 700
if salary> 50000 & cibil>750 -> Instant Approval
Otherwise -> rejected
'''

# salary = int(input("Enter your salary: "))
# cibil_score = int(input("Enter your Cibil Score: "))

# if salary > 25000 and cibil_score > 700:
#     if salary > 50000 and cibil_score > 750:
#         print("Congratulations! Your loan is approved instantly.")
#     else:
#         print("We will let you know about the loan approval soon.")
# else:
#     print("Loan rejected.")

'''
WAP to check whether a year is leap year or not.
'''

# year = int(input("Enter a year: "))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(year, "is a leap year.")
# else:
#     print(year, "is not a leap year.")

'''
WAP to take a character from the user and convert it into lowercase if it is in uppercase or vice-verse.
Make sure no special  characters are allowed.
'''

# char = input("Enter a character: ")

# result = ''


# if(ord(char)>=65 and ord(char)<=90):
#     result = chr(ord(char)+32)
# elif(ord(char)>=97 and ord(char)<=122):
#     result = chr(ord(char)-32)
# else:
#     print("Invalid character entered.")

# print("The converted character is:", result )

'''
Achieve the desired output for the below given input:


## INPUT: RAhul@123Gh
## OUTPUT: raHUL@123gH

## You can't use any inbuilt function.
'''

# input_str = "RAhul@123Gh"
# output_str = ""

# for char in input_str:
#     if ord(char) >= 65 and ord(char) <= 90:  # Uppercase
#         output_str += chr(ord(char) + 32)
#     elif ord(char) >= 97 and ord(char) <= 122:  # Lowercase
#         output_str += chr(ord(char) - 32)
#     else:
#         output_str += char  
# print("Output:", output_str)

'''
1.
## input: [10, 2.2, 5, 'Hello', [100,200], 99.9]
## output: 99.9

2.
## input: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
## output: {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

3.
## input: ('Hello', 'Hi', 20, 40.2, 9.6j, [1,2], 'PYTHON', 'JECRC', (1, 2, 3))
## output: {'Hello': 'l', 'Hi': 'Hi', 'PYTHON': 'PN', 'JECRC': 'C', (1, 2, 3): 2}
'''

# coll = [10, 2.2, 5, 'Hello', [100,200], 99.9]
# max = coll[0]

# for i in coll:
#     if type(i) in [int, float]:
#         if i > max:
#             max = i
# print("Maximum value in the collection is:", max)
# ----------------------------------------------
# coll = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# new_coll = {}
# for i in coll:
#     new_coll[coll[i]] = i
# print(new_coll)
# ---------------------------------------------
# coll = eval(input("Enter a collection: "))
# new_coll = {}
# for i in coll:
#     if type(i) in [str, tuple]:
#         if len(i) % 2 == 0:
#             new_coll[i] = i[0] + i[-1]
#         else:
#             new_coll[i] = i[len(i)//2]
# print(new_coll)

## Whenever python interprereter will encounter "break" keyword it will simply stop its execution on this particular line and make the interpreter to go outside of the loop. In future, control will never go inside tha same loop again.


# coll = [10, 20, 30, 40, 50, 'HI']
# i, flag = coll[0], True

# for j in coll:
#     if type(i) == type(j):
#     #     (flag = True
#     # else:
#     #     flag = False)
#           flag = False
#           break

# if flag:
#     print("Homogeneous collection.")
# else:
#     print("Heterogeneous collection.")

# ----------------------------------------------

if True:
    ## I don't have statement block.
    pass

for i in range(10):
    pass

def addTwoNums():
    pass

print("Transylvania!")
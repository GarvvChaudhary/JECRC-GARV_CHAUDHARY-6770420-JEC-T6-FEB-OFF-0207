# '''
# It is a type of statement which controls the flow of the execution of the program. 
# '''
# ## Conditional Statement: Based upon one condition, the execution of the program is decided.
# '''
# 1. if statement (Simple if)
# 2. if-else statement
# 3. elif statement
# 4. Nested if statement'''

# ## WAP to check whether the username & password is correct or not. If correct print login successfuly completed. If not, do nothing.

# user = {
#     'username': 'user123',
#     'password': '****'
# }
# un = input('Enter username: ')
# pswd = input('Enter password: ')

# ## If the condition is True, then only if block will be executed.
# if un == user['username'] and pswd == user['password']:
#     print('Login successfully completed.')

# # print('Program got ended.')

## elif statement
## When you have multiple conditions; multiple statement vlocks;
## at least one if condition should be there.


## WAP in python to take a character from the suer and check whether it is a vowel or, consonent or, special character.

'''
1. Take a character from the user.
2. Apply the conditions one by one.
'''

# chr = str(input('Enter a character: '))
# if chr in 'aeiouAEIOU':
#     print('It is a vowel.')
# elif chr in '0123456789':
#     print('It is a digit.')
# elif chr in '!@#$%^&*()':
#     print('It is a special character.')
# elif chr not in 'aeiouAEIOU':
#     print('It is a consonent.')


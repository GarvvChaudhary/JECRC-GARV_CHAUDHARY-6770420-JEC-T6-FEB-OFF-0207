#Function for string Data Type
'''
lower ,upper ,capitalize,title,strip,lstrip,rstrip,replace,index,split, join, startwith, endswith, isdigit, islower,isupper,


'''

s="Python1234"
print(s.lower())

result=s.upper()
t1=result.title()
print(t1)
#Strip
print(" ".strip())
strp="frejfer cwew".strip('w')
print(strp)
#lstrip
print("Fersd".lstrip('d'))
#rstrip
print("fersds".rstrip('s'))

#replace

print("Python".replace('P','y'))
print("fersds".replace('s','i'))

#index
print("Python Programming".index('gr',0,14))

#Find
print("PyhonProgramming".find("mm",0,16))

#split
res="Python Programming".split()
print(res)

#Join
srt=' '.join(res)
print(srt)

#startswith
srt.startswith("Py")

#isdigit
num="1234"
num1="dc124"
print(num.isdigit())
print(num1.isdigit())

#isalpha
alp="adwede"
print(num.isalpha())
print(alp.isalpha())

#isendswith
alpd="dewedw"
print(alpd.endswith("dw"))

#Functions for List DataTypes
'''
append, insert,extend,pop,remove
'''

l1=[1,324,34,'Python']
l1.append(32)
l1.insert(2,'Pro')
print(l1)
l1.pop(3)
l1.remove(1)
l1.pop()
print(l1)
l1=[1,324,34,'Python']
l1.index(34)
l2=[23,45,31,65,62]
l2.sort(reverse=True)
print(l2)
l1.clear()
print(l1)

#tuple
t=(32,54,23,86,32)
print(t.index(54))
print(t.count(32))

#set
a={1,3,5.4,4,5,6}
a.add(3)
print(a)
s={1,2,True,False,0}
b=(1,34,5,3+5j)
s.add(b)
s.remove(2)
print(s)
s.discard(2)
b={1,34,5,3+5j}
c={6,8,3,2}
s3=b.union(c)
print(s3)
print(s3.pop())
print(s3.pop())

#dict
d={1:12,3:43,(1,2,3):(32,3)}

dict={
    "username":"user123",
    "password":"*******",
    "location":"IN"
}
print(dict.popitem())

dict["password"]="12345"
dict.update({"password":"09765"})
print(dict.keys())
print(dict.values())
print(dict.items())
print(dict)

#Packing

#Single Packing
def add_nums(*args):
    args=list(args)
    print(args,type(args))
    sum=0
    for i in args:
        sum+=i
    print(f'Addition:{sum}')

add_nums(1,2,3,4,5,6)        


# #TASK1
# def n(*args):
#     sum=0
#     datatype=[int,float]
#     for i in args:
#         if type(i) in datatype:
#              sum+=i
       
#     print(f'Addition:{sum}')

# n(1,2,4,5.0,2.1,True,False)  

# def print_num(**kwargs):
#     print(kwargs)
# print_num(username='usern123',password="****",logged_in=["Andriod","windows","Linux"])

#unpacking
# n(*eval(input("Enter a list of values: ")))

#create a function which will return a list of prime numbers 
def isPrime(n):
    if n<2: return False
    for i in range(2,n-1):
        if n%i==0:
            return False;
    return True

def find_Prime_num(*args):
    prime=[]
    for i in args:
        if isPrime(i):
            prime.append(i)
    print( prime)        

find_Prime_num(*eval(input("Enter numbers:")))
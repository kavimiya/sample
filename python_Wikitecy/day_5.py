#math packege
import math
print("math package ")
print(math.sqrt(22))
print(math.ceil(6.577))
print(math.floor(6.577))#this using hole number 
print(math.factorial(4))
print(math.fabs(-4)) #only positive number
print(math.pow(4,3))#power value 
print(math.log10(40))#this log value 
print(math.pi)#this contanct valuue
print(math.e)
print("-------------------------------------------------")

#try block statment

try:
    q=10/30
except Exception as qq:#this use error skipped 
    print(qq)
else:#no error run this codr else block
    print(q)
finally:#this using exception bolck and else block not work or work this block is working
    print("thaks you")


print(len(dir(locals()['__builtins__'])))#this exception all error
print(dir(locals()['__builtins__']))

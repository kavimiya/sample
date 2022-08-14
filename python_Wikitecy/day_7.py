#use ord function

a='a'
b=ord(a)
print(b)#this letter to unicode number show 
print(type(b))

#use chr function
a=97
b=chr(a)#this unicode to chat 
print(b)
print(type(b))

#this using end  this same line output
print(a,end='')
print(b)
print(b)

#this sep using 
print(4,5,6,sep=',')


#today solve
#Taking length and breadth as input
l,b = map(float,input().split(' '))

#Calculating area
area = l * b

#print the area
print(int(area))












# showing logical operation
# or (returns True)
print(True or False)

# showing logical operation
# and (returns False)
print(False and True)

# showing logical operation
# not (returns False)
print(not True)

# using "in" to check
if 's' in 'geeksforgeeks':
	print("s is part of geeksforgeeks")
else:
	print("s is not part of geeksforgeeks")

# using "in" to loop through
for i in 'geeksforgeeks':
	print(i, end=" ")

print("\r")

# using is to check object identity
# string is immutable( cannot be changed once allocated)
# hence occupy same memory location
print(' ' is ' ')

# using is to check object identity
# dictionary is mutable( can be changed once allocated)
# hence occupy different memory location
print({} is {})


# Using for loop
for i in range(10):

	print(i, end = " ")
	
	# break the loop as soon it sees 6
	if i == 6:
		break
	
print()
	
# loop from 1 to 10
i = 0
while i <10:
	
	# If i is equals to 6,
	# continue to next iteration
	# without printing
	if i == 6:
		i+= 1
		continue
	else:
		# otherwise print the value
		# of i
		print(i, end = " ")
		
	i += 1

# Python program to illustrate if-elif-else ladder
#!/usr/bin/python

i = 50
if (i == 10):
	print ("i is 10")
elif (i == 20):
	print ("i is 20")
else:
	print ("\ni is not present")

# A Python program to return multiple
# values from a method using class
class Test:
	def __init__(self):
		self.str = "sathish"
		self.x = 20.0

# This function returns an object of Test
def fun():
	return Test()
	
# Driver code to test above method
t = Test()
print(t.str)
print(t.x)


# A Python program to return multiple
# values from a method using tuple

# This function returns a tuple
def fun():
	str = "top 1 company"
	x = 44
	return str, x; # Return tuple, we could also
					# write (str, x)

# Driver code to test above method
str, x = fun() # Assign returned tuple
print(str)
print(x)


# A Python program to return multiple
# values from a method using dictionary

# This function returns a dictionary
def fun():
	d = dict();
	d['str'] = "GeeksforGeeks"
	d['x'] = 20
	return d

# Driver code to test above method
d = fun()
print(d)


# Python3 program to
# demonstrate instantiating
# a class


class Dog:
	
	# A simple class
	# attribute
	attr1 = "1"
	attr2 = "33"
	# A sample method
	def fun(self):
		print("first", self.attr1)
		print("secod", self.attr2)

# Driver code
# Object instantiation
Rodger = Dog()

# Accessing class attributes
# and method through objects
print(Rodger.attr1)
Rodger.fun()

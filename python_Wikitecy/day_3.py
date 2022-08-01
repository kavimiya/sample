a=[22,5,77,21,10,88]
print(a)
a.sort()# use sort  function 
print(a)

b=['v','t','s','a','g','b','c','j']
print(b)
b.sort()#order by letter and number 
print(b)

#reverse order
c=[22,99,3,22,88,55]
print(c)
c.sort(reverse=True)#this using reverse order 
print(c)

#key use len
d=['aa','mm','y','bb','d']
print(d)
d.sort(key=len) # use function short to long
print(d)


#this use  long to short
s=['aa','s','ccc','dd','b']
print(s)
s.sort(key=len,reverse=True)#use long to short 
print(s)

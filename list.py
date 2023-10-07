a = []
b = ()
c = {}
print(type(a))
print(type(b))
print(type(c))
                # we can know datatype of variable using type() function
a = [2,4,6,8,0]
b = (1,3,5,7,9,11,13,15,17,19)
c = {1,2,3,4,5}
d = {'name' : "Sanju",'addr' : 'Hivare Korda', 'Gender' : 'Female',101 : 200}

print(a)
print(b)
print(c)
print(d)
                # We can  Access values by indexing :

print(a[2])
print(a[-1])    # Negative Indexing 
                
print(d['Gender'],d[101])       # We can't get value by index in dict.
                                # we should get value by its key..

x = 10
x = 20 
print(x)       

w = x,y,z = 3,4,5            # Multiple variable Declaration in one line 
print(w)

S = 50
s = 25                        # Python is Case Sensitive..

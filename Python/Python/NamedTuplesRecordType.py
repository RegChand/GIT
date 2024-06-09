from recordtype import recordtype

Point = recordtype('Point',['x', 'y'], default=3) #if no value then default is used
P = Point (1,3)
print(P) #values assigned to P
print(P.x) #value assigned to X
print(P.y) #value assinged to Y
P.x = 9 #change value of X
print(P.x)
from collections import namedtuple
Vision = namedtuple('Vision',['left', 'right'])
print(issubclass(Vision,tuple)) #check if tuple is true
vision = Vision(9.5, 8.8) #assign variables to tuple
print(vision.left)
print(vision.right)
print(vision[0]) #same as left 
print(vision[1]) #same as right
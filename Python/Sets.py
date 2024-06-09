#We use sets when we do not want duplicates. 
primenum = set() #creates an empty set
primenum.add(2)
primenum.add(3)
primenum.add(5)
print(primenum) #prints {2,3,5}
primenum.add(1)
primenum.remove(1)
print(3 in primenum) #returns true as 3 is in the list
print(3 not in primenum) #returns false as 3 is there in the list
primenum.add(3) #does not allow duplicates
print(primenum)
anotherprime = set([5,7,11,13]) #fast way to create new sets
print(anotherprime) #prints {13, 11, 5 7}
newprime = primenum | anotherprime #Union the two sets
print(newprime) #5 is removed from the set as it was a duplicate 
print(primenum & anotherprime) #returns 5 as this is the duplicate value in both sets {5}
print(newprime - anotherprime) #different operator 

#frozen set
small_prime = frozenset([2,3,5,7]) #we cannot add or remove values from frozen set
print(small_prime)
small_prime.add(11) #Will give an error
#interset and union etc is allowed but cannot add or remove. 
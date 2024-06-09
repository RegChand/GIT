#create a standard list in Python
a = list(range(11))
print(a) 
a.append(11) #Adds 11 to the end of the list
a.extend([12, 13]) #extend the list by few more values 
a.insert(10,36) #adds value 36 at position 10
a.remove(36) #removes values 36
a.reverse() #reverse the order of values in the list
a.pop() #removes the last value from the list
a.sort() #sorts the list of values
a.clear() #removes all values from the list


#Create a list from python using itemgetter
from operator import itemgetter
a = [(5,3), (1,3), (1,2), (2,-1), (4,9)]
print(sorted(a)) #prints a sortd list
print(sorted(a, key=itemgetter(0))) #sorting is done only on the first element
print(sorted(a, key=itemgetter(0,1)))#sort on the first element at position zero then those on position 1
print(sorted(a,key=itemgetter(1))) #sorts on position 2 first then second element of each tuple 
print(sorted(a,key=itemgetter(1), reverse=True))#sorts on position two but reverse the order
#create a dictionary
d = {} #empty diictionary
d['a'] = 1 # {key, value} pairs
d['b'] = 2
print(d) #prints {'a': 1, 'b': 2}
print(d['a']) #what is the value of a
del d['a'] #delete a
d['c']=3 #added c
print(d) #shows {'b': 2, 'c': 3}
print('c' in d) #returns true
d.clear() #removes everything. 

d = dict(zip('hello', range(5))) #creates a dictionary with hello word and range is 5
print(d)
print(d.keys()) #prints the key value h,e,l,o
print(d.values()) #prints values 0 1 3 4
print(d.items()) #prints ([('h', 0), ('e', 1), ('l', 3), ('o', 4)]) entire dictionary
print(3 in d.values())
print(('o', 4) in d.items())
d.popitem() #removes a random item
d.pop('l') #removes item with key 1
d.pop('not-a-key', 'default-value')
d.update({'another': 'value'})
print(d)
print(d.get('a'))
print(d.get('a', 177))
d.setdefault('a', 1)
print(d)
print(d.get(''))
#Just adding a comment
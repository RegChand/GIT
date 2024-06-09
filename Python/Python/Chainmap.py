#great for linking a number of mappings so that can be treated as a single unit. 
#underlying mapping is stored in a list. 
#the list is public and can be accessed or updated using map attribute
#writes updates delete only work in first mapping. 

from collections import ChainMap
default_connection = {'host': 'localhost', 'port': 145679}
connection = {'port': 5678}
conn = ChainMap(connection, default_connection) #map creation 
print(conn['port']) #returns 5678 as port value is found
print(conn['host']) #returns localhost as host is foudn from the second value. 
print(conn.maps) #returns the mapping
conn['host'] = 'packtpub.com' #adding a host
print(conn.maps)
del conn['port'] #deletes port information
print(conn.maps)
print(conn['port']) #now port is fetched from the second dictionary
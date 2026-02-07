s = set() #empty set

t = {1,2,5,3,5,7,5,5}
u = {3,4,5,6,7,8,9,0}
print(t) 
print('length: ',len(t))

t.remove(5)
print(t)

print('union:',t.union(u))
print('intersection:',t.intersection(u))
print(t.issubset(u))

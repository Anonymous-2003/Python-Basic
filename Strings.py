#String slicing and indexing

name = "Avishek Basyal"
print(len(name))
print(name[1:len(name):2]) # prints  from 1 to length with increment of 2 
print(name[-1::-1]) # prints from last index to 0th index with decrement of 1

#string iteration

for i in range(len(name)-1,-1,-1): #iterating from last index to -1th index
    print(name[i])

print()
for i in name:
    print(i)
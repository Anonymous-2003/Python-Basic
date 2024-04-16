# set are unordered(i.e while printing element may be in random order) and unindexed collection of data. 
# defined under curly bracket
# sets are iterable,mutable and has no duplicate element    

s = {10,20,30,40,50,99}
s.add(100)
print(s)
print(s.pop()) 
s.remove(30)
s.discard(10)
print(s)
l = ['a','e','i','o','u']
s.update(l)
print(s)

s.clear()
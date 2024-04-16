# Tuple is a collection which is ordered and inmutable. 
# iterating through tuple is faster than list
# defined under parenthesis (). Single element inside parenthesis is not considered as tuple

#min,max,count,index,sum
t = (10,20,30,40,50)
print(t[2])
for i in range(len(t)):
    print(t[i])\
    
# functions in tuple
print(min(t))
print(max(t))
print(t.count(20))  # return the index number in which 20 is stored
print(t.index(50))  # same as count
print(sum(t))       # returns the sum of all the integer or float inside tuple
print(sum(t,12))    # by default the sum is 12 
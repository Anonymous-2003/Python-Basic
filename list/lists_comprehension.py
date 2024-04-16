# l = [n for n in range(1,101)] # in first 'n' data is stored and second 'n' is for iteration
#                               # variable should be same under list comprehension(i.e 'n') 
# print(l)


celcious = [37,-40,30,0]
fahrenheit = [(9/5)*temp+32 for temp in celcious]
print (fahrenheit)


num = [n**2 for n in range(1,100) if n % 5 ==0]  # storing and squaring to first n only if divisible by 5
print (num)


# list comprehension using condition
# l = [m for m in range(1,101) if m%2 == 0]
# print(l)
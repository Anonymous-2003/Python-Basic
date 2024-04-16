import random
# for generating integers

random_integer = random.randint(1,100) # generates random integer between  1 and 100 both inclusive
print(random_integer)

#for generating random decimal numbers

random_decimal = random.random() # This generates random decimal numbers between 0 and 1
print(round((random_decimal*10),2)) # multiplying by 10 generates decimal numbers between 0 and  10

l = ['avi','asd','fgh']
print(random.choice(l))

print(random.randrange(1,10)) # random from 1 to 10. 1 included and 10 not included

print(round(random.uniform(1,100),2))  # returns a random float number between two given characters
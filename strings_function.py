s = "WelCOme to THe woRlD of ARtifiCiaL IntelliGence"
l =s.lower()        # makes everything in lower case
u =s.upper()        # makes everything in upper case
t =s.title()        # only first letter of every word will  be capitalized
c =s.capitalize()   # only first letter is capatilize and other will be in lower case
print(l)
print(u)
print(t)
print(c)

n = "Hello223"
print(n.isalnum())

x=chr(90) # converts integer to character, so it returns character string
print(type(x),x)
y = ord('a') # takes charaacter and return integer
print(type(y),y)
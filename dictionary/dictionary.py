# unordered data type,work on key/pair and is defined under curly bracket
# each key and value is seprated by comma at last


# here name,address and age are key and on right of them are value. 
# keys can't be of same name but values can be

d = {
        'name':'Avishek Basyal',
        'address':'Sandhikharka, Arghakhanchi',
        'age':21,
        'gender':'male'

    }

# Accessing elements from dictionary

print(d['name'])    # Prints value of given key.
print(d)            # Prints whole dictionary 


# Iterating through dictionary
for i in d:
    print(i)  # it will print key only
    print(d[i]) # it will print value only


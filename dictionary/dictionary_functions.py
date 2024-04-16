d = {
        'name':'Avishek Basyal',
        'address':'Sandhikharka, Arghakhanchi',
        'age':21,
        'gender':'male'

    }

n = d.get('name')
    # or
n = d['name']
print(n)

for a in d.keys():    # stores only the keys from d to a
    print(a)

for a in d.values():    
    print(a)    # print only values

for a,b in d.items():   # key is stored in first variable and value is stored in second variable
    print(a,b)

del d['name'] 
    # or
d.pop('age')
print(d)

dic = dict(name = 'Avishek', fees = 2000)  # creating dictionary using dict keyword
print(dic)
